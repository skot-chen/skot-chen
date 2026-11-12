<p align="center">
  <img src="assets/catmain.png" width="300" alt="a cream-and-white cat lying down" />
</p>

<h2 align="center">嗨，我是 skot 👋</h2>

<p align="center">
  做<b>小而顺手</b>的工具：桌面小应用、打开就能用的网页工具、运维自动化小服务。<br/>
  和 AI 编程助手一起开发，从想法、设计、测试到发布，一个人把东西做完整。<br/>
  <sub><i>I build small tools that just work — desktop apps, zero-install web tools and ops automation.</i></sub>
</p>

---

### 🔭 我在做什么 · What I do

- **桌面小应用**：轻量、常驻、不打扰，Windows 和 macOS 都能用
- **零安装网页工具**：纯前端，数据只留在浏览器，打开链接就能用
- **运维自动化**：日志归类、工单分析、API 负载均衡
- **AI 辅助开发**：自动测试 + CI + 一键发布，每次改动都先验证再上线

### 🖥️ 桌面应用 · Desktop

**[cat-clock](https://github.com/skot-chen/cat-clock)**：两只住在桌面上的猫，各自显示一个城市的时间
- 两个时区一眼看清，到点提醒「该打电话啦」
- 猫会走会跑，主人睡觉时它也睡；点它会跳会叫，摸它会呼噜，可以拖到任意位置
- Windows + macOS 安装包 · `Rust` `Tauri` `JavaScript` · [下载](https://github.com/skot-chen/cat-clock/releases/latest)

**[OpenCodeCat](https://skot-chen.github.io/OpenCodeCat/)**：桌面上的一只像素小猫，顺手看一眼 AI 用量
- 平时只显示月度百分比，鼠标移上去展开 5 小时 / 周 / 月三档进度
- 点一下看重置时间和完整额度，可拖到屏幕任意位置
- macOS · `Swift` · [下载](https://github.com/skot-chen/OpenCodeCat/releases/latest)

**[bilingual-board](https://github.com/skot-chen/bilingual-board)**：中英双语聊天板，适合两个人共用一台电脑
- 每条消息自动翻译，英文错误用红笔标出并解释原因
- 免费离线的语法检查，不用账号，聊天记录只存在本机
- Windows + macOS · `JavaScript`

### 🌐 网页工具 · Web tools（打开就能用）

**[Ops Drills](https://skot-chen.github.io/ops-drills/)**：在浏览器里写 Python、自动判对错的练习平台
- Python 直接在网页里运行（WebAssembly），不用装任何东西
- 每次发布前，所有例题和答案都会先用真的 Python 跑一遍验证
- 间隔复习、收藏、进度导出 · `JavaScript` `Pyodide` `GitHub Actions` · [源码](https://github.com/skot-chen/ops-drills)

**[Daily Words](https://skot-chen.github.io/daily-words/)**：背单词 + 默写网站
- 认词卡片、看中文默写、听写、打印成 A4 练习纸
- 间隔复习（1、2、4、7、15、30 天），手机电脑都能用
- 新词只要加一个 JSON 文件，CI 自动校验并发布 · `JavaScript` · [源码](https://github.com/skot-chen/daily-words)

**[log-kb-lite](https://skot-chen.github.io/log-kb-lite/)**：纯网页的日志归类分析工具
- 导入语料 → 关键字与分类 → 分析 → 结果验收与导出
- 数据只在浏览器本地处理；也有离线桌面版 · `JavaScript` `Python` · [源码](https://github.com/skot-chen/log-kb-lite)

### ⚙️ 运维与后端 · Ops & backend

**[ticket-governance-demo](https://skot-chen.github.io/ticket-governance-demo/dashboard/)**：工单治理工作流 + 在线看板
- 字段标准化 → 时长 / 类型 / 处理办法三维分析 → KPI → P0/P1/P2 优先级矩阵 → PDCA 闭环
- 附 Excel 模板，可直接套用到真实工单 · `JavaScript` · [源码](https://github.com/skot-chen/ticket-governance-demo)

**[modelscope-balance](https://github.com/skot-chen/modelscope-balance)**：大模型 API 多 Key 负载均衡服务
- 多个 API Key 轮换转发，自动健康检查，实时统计
- 反向代理连接池复用，分级日志 · `Go` `Docker`

### 🧰 技术栈 · Stack

`Python` · `JavaScript` · `Go` · `Rust / Tauri` · `Swift` · `Docker` · `GitHub Actions` · `GitHub Pages` · `Claude Code`

### 📫 找到我 · Find me

[Blog](https://kuake.qzz.io) · [GitHub](https://github.com/skot-chen)
