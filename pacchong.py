import requests
from bs4 import BeautifulSoup

# 目标网页URL
url = 'https://www.cwl.gov.cn/ygkj/wqkjgg/ssq/'

# 发送HTTP请求
response = requests.get(url)

# 确保网页请求成功
if response.status_code == 200:
    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取你感兴趣的数据，例如所有段落文本
    paragraphs = soup.find_all(attrs={"class":"qiu"})
    for p in paragraphs:
        print(p.get_text())
else:
    print(f"Error: {response.status_code}")