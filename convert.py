import json
import re
from concurrent.futures import ThreadPoolExecutor

# 读取README.md文件的内容
with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()
    # 当读取到包含'### 🚫 已失效'的行时停止读取
    content = content.split('<tbody>')[1]
    content = content.split('</tbody>')[0]
    content = re.sub(r'\s+', ' ', content).strip()
#print(content)
pattern = re.compile(r'<tr.*?>(.*?)<\/tr>')
urls = pattern.findall(content)
print(urls[0])
#pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+(?=\])')
# 在内容中找到所有的URL
#urls = pattern.findall(content)
# 移除URL末尾的'/'并合并相同的URL
unique_urls = []
def det_sine(html):
    p = re.compile(r'<td>(\d+)</td>\s*<td>\s*<a href="([^"]+)" target="_blank">[^<]+</a>\s*<br>\s*</td>\s*<td>\s*([\W\s]+)\s*</td>\s*<td>(\d{4}-\d{2}-\d{2})</td>')
    p = p.findall(html)
    return p
for i in urls:
    unique_urls.append(det_sine(i))
    urls = []
for i in unique_urls:
    for h in i:
        h=list(h)
        h[2] = re.sub(r'\s+', '',h[2])
        urls.append(h)

print(urls)
"""
for url in urls:
    url = url[:-1] if url.endswith('/') else url
    if url not in unique_urls:
        unique_urls.append(url)
print(unique_urls)
"""
# 将URL保存到urls.json文件中
with open("urls.json", "w") as file:
    json.dump(urls, file,indent=4)
