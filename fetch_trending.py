import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = "https://github.com/trending"
headers = {"User-Agent": "Mozilla/5.0"}

resp = requests.get(url, headers=headers, timeout=10)
soup = BeautifulSoup(resp.text, "html.parser")

# 抓取时间
now = datetime.now()
fetch_time = now.strftime("%Y-%m-%d %H:%M:%S")

repos = []
for repo in soup.select("article.Box-row")[:10]:
    name = repo.select_one("h2 a").get_text(strip=True).replace("\n", "").replace(" ", "")
    desc_tag = repo.select_one("p")
    desc = desc_tag.get_text(strip=True) if desc_tag else "无描述"
    stars = repo.select_one("a[href$='/stargazers']")
    star_count = stars.get_text(strip=True) if stars else "0"
    lang_tag = repo.select_one("span[itemprop='programmingLanguage']")
    lang = lang_tag.get_text(strip=True) if lang_tag else "未知"

    repos.append({
        "name": name,
        "description": desc,
        "stars": star_count,
        "language": lang,
        "fetch_time": fetch_time
    })

result = {
    "date": now.strftime("%Y-%m-%d"),
    "fetch_time": fetch_time,
    "repos": repos
}

with open("trending.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"✅ 已保存 {len(repos)} 个仓库到 trending.json")
print(f"🕐 抓取时间: {fetch_time}")