import aiodns
import asyncio
from aiodns.error import DNSError

async def get_record(domain):
    """
    解析域名的各种 DNS 记录
    
    Args:
        domain: 要解析的域名
    Returns:
        dict: 包含各种 DNS 记录的字典
    """
    #定义要查询的类型
    record_types = [
        ("query","A"),
        ("query","AAAA"),
        ("query","CNAME"),
        ("query","MX"),
        ("query","NS"),
        ("query","TXT"),
        ("query","SRV"),
        ("query","CAA"),
    ]
    #初始化解析器
    resolver=  aiodns.DNSResolver()
    #空字典收集数据
    records = {}

    for method, record_type in record_types:
        print(f"当前{records}\n")
        try:
            result = await getattr(resolver, method)(domain, record_type)
            records[record_type] = result
        except DNSError as e:
            records[record_type] = f"No {record_type} record found: {str(e)}"
        except Exception as e:
            records[record_type] = f"Error getting {record_type} record: {str(e)}"
    
    return records

async def main():
    domain = "aliyun.com"
    a_records = await get_record(domain)
    print(f"记录{domain},为：{a_records}")

asyncio.run(main())


