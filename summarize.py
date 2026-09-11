import json
import requests

# ⚠️ 替换成你的智谱 API Key
API_KEY = "78c8f06346204dee954f74d474d67d49.kGaAVm2sU9KbB1NA"
API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

# 1. 读取抓取结果
with open("trending.json", "r", encoding="utf-8") as f:
    data = json.load(f)

repos = data["repos"]
fetch_time = data["fetch_time"]

# 2. 拼成文本给 AI
repo_text = ""
for i, r in enumerate(repos, 1):
    repo_text += f"{i}. {r['name']} | {r['language']} | ⭐{r['stars']}\n   {r['description']}\n"

# 3. 构造 Prompt
prompt = f"""你是一个技术资讯编辑。以下是 {fetch_time} 抓取的 GitHub Trending 仓库列表。

请你：
1. 过滤掉纯教程、课程、简历模板、Awesome 列表类项目
2. 按"对一线开发者的实用度"重新排序
3. 每个项目用一句话点评，说明它解决什么痛点、比同类强在哪
4. 每个项目必须带上 star 数，格式为：项目名 | ⭐星数 | 点评
5. 最终输出 8 条以内，用 Markdown 格式

仓库列表：
{repo_text}
"""

# 4. 调用智谱 API
resp = requests.post(
    API_URL,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "glm-4-flash",
        "messages": [{"role": "user", "content": prompt}]
    },
    timeout=60
)

result = resp.json()
summary = result["choices"][0]["message"]["content"]

# 5. 保存结果
with open("summary.md", "w", encoding="utf-8") as f:
    f.write(f"# GitHub Trending 每日总结\n\n")
    f.write(f"**抓取时间**：{fetch_time}\n\n")
    f.write(summary)

print("✅ 总结已保存到 summary.md")
print("=" * 50)
print(summary)