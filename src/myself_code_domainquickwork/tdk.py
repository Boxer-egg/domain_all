import requests
from bs4 import BeautifulSoup

url = "https://bilibili.cn"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')

# 打印实际编码
print("Response encoding:", r.encoding)


# 手动解码
raw_content = r.content
try:
    # 尝试不同编码
    encodings = ['utf-8', 'gb2312', 'gbk', 'gb18030', 'big5']
    for encoding in encodings:
        try:
            decoded_content = raw_content.decode(encoding)
            soup = BeautifulSoup(decoded_content, 'lxml')
            #print(f"{decoded_content[:1500]}")
            title = soup.title.text if soup.title else 'Undetected,title'
            print(f"成功使用 {encoding} 解码:", title)
            break
        except UnicodeDecodeError as e:
            print(f"{encoding}失败原因：{e}")
except Exception as e:
    print("解码意外失败:", str(e))



description_tag = soup.find('meta',attrs={"name":"description"})
keywords_tag = soup.find('meta',attrs={"name":"keywords"})

print(description_tag,keywords_tag)