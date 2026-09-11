# 📬 GitHub Trending Daily

每天自动抓取 GitHub Trending 项目，用 AI 筛选、排序、点评后推送到邮箱。

## ✨ 功能

- 每天定时抓取 GitHub Trending 热门项目
- 调用智谱 AI 过滤水文、重新排序、生成一句话点评
- 通过邮件自动推送到你的邮箱（HTML 格式）
- 支持手动触发，随时获取最新总结
- 抓取失败自动重试 3 次

## 🛠️ 技术栈

- Python 3.13
- requests + BeautifulSoup（抓取和解析）
- 智谱 AI API（内容筛选和总结）
- GitHub Actions（定时调度）
- SMTP（邮件推送）

## 🚀 快速开始

### 1. Fork 本仓库

### 2. 配置 Secrets

在仓库 Settings → Secrets and variables → Actions 里添加：

| Name | 说明 |
|------|------|
| ZHIPU_API_KEY | 智谱 API Key |
| MAIL_USER | 发送邮箱（如 xxx@qq.com） |
| MAIL_PASS | 邮箱授权码（不是登录密码） |
| MAIL_TO | 接收邮箱 |

### 3. 手动触发

在 Actions 页面点击 Run workflow，即可运行一次。

### 4. 本地运行

```bash
pip install requests beautifulsoup4
python fetch_trending.py
python summarize.py
```

## 📁 项目结构

```
├── fetch_trending.py           # 抓取 GitHub Trending
├── summarize.py                # 调用 AI 总结 + 邮件推送
├── .github/workflows/daily.yml # GitHub Actions 定时任务
├── .gitignore
└── README.md
```

## 📬 推送效果

每天早上 8 点（北京时间），邮箱会收到一封 HTML 格式的总结邮件，包含：
- 抓取时间
- AI 筛选后的 8 个项目
- 每个项目的 star 数和一句话点评

## 👨‍💻 作者

s1huan1an