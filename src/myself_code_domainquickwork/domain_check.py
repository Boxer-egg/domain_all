import requests
from bs4 import BeautifulSoup

#url = "https://httpbin.org"
url = 'https://west.cn'

hds={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

r = requests.get(url,headers=hds)
html_doc = r.text
soup = BeautifulSoup(html_doc,"lxml")

try:
    title = soup.title.text
    if title:
        title=title.encode("utf8","ignore").decode()
except AttributeError:
    title =None

print(title)

