"""Rewrites the 'recent releases' list in README.md from the owner's public repos.
Run by .github/workflows/update.yml every day. Stdlib only. Uses GITHUB_TOKEN if set."""
import json
import os
import re
import urllib.request

USER = "skot-chen"
README = os.path.join(os.path.dirname(__file__), "..", "README.md")
LIMIT = 5


def get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "profile-readme"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main():
    repos = get(f"https://api.github.com/users/{USER}/repos?type=owner&per_page=100")
    rels = []
    for repo in repos:
        if repo["fork"] or repo["private"] or repo["name"] == USER:
            continue
        for rel in get(f"https://api.github.com/repos/{USER}/{repo['name']}/releases?per_page=3"):
            if rel["draft"] or rel["prerelease"]:
                continue
            rels.append((rel["published_at"] or rel["created_at"], repo["name"], rel["tag_name"], rel["html_url"]))
            break  # newest release per project only
    rels.sort(reverse=True)
    lines = [f"- [{name} {tag}]({url}) · {when[:10]}" for when, name, tag, url in rels[:LIMIT]] or ["- 暂无"]
    text = open(README, encoding="utf-8").read()
    new = re.sub(r"(<!-- releases:start -->\n).*?(\n<!-- releases:end -->)",
                 lambda m: m.group(1) + "\n".join(lines) + m.group(2), text, flags=re.S)
    if new != text:
        open(README, "w", encoding="utf-8", newline="\n").write(new)
        print("README updated")
    else:
        print("no change")


if __name__ == "__main__":
    main()
