import requests
from bs4 import BeautifulSoup

url = "https://www.bilibili.cn"
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

def check_dn_tdk(domain):
    """
    查询域名tdk
    """
    raw_content = r.content #字节码.text 存的是.content 编码后的字符串
    try:
        # 尝试不同编码
        encodings = ['utf-8',  'gb18030','gb2312', 'gbk', 'big5']
        for encoding in encodings:
            try:
                decoded_content = raw_content.decode(encoding)
                soup = BeautifulSoup(decoded_content, 'lxml')
                title_tag = soup.title.text if soup.title else '未发现标题'
                description_tag = soup.find('meta',attrs={"name":"description"})
                keywords_tag = soup.find('meta',attrs={"name":"keywords"})
                print(
                    f"成功使用 {encoding} 解码: \
                    标题：{title_tag}\n, \
                    描述：{description_tag}\n,\
                    关键字：{keywords_tag}\n")
                break
            except UnicodeDecodeError as e:
                print(f"{encoding}失败原因：{e}")
    except Exception as e:
        print("解码意外失败:", str(e))


def check_dn_ssl(domain):
    pass