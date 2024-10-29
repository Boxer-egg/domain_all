import asyncio
import aiodns
from aiodns.error import DNSError

async def resolve_dns_records(domain):
    """
    解析域名的各种 DNS 记录
    
    Args:
        domain: 要解析的域名
    Returns:
        dict: 包含各种 DNS 记录的字典
    """
    resolver = aiodns.DNSResolver()
    records = {}
    
    # 定义要查询的记录类型
    record_types = [
        ('A', 'query'),
        ('AAAA', 'query'),
        ('CNAME', 'query'),
        ('MX', 'query'),
        ('NS', 'query'),
        ('TXT', 'query'),
        ('PTR', 'query'),
        ('SOA', 'query')
    ]
    
    for record_type, method in record_types:
        try:
            result = await getattr(resolver, method)(domain, record_type)
            records[record_type] = result
        except DNSError as e:
            records[record_type] = f"No {record_type} record found: {str(e)}"
        except Exception as e:
            records[record_type] = f"Error getting {record_type} record: {str(e)}"
    
    return records

async def format_dns_results(domain):
    """
    格式化 DNS 解析结果为可读形式
    """
    results = await resolve_dns_records(domain)
    
    formatted_output = f"DNS records for {domain}:\n"
    for record_type, result in results.items():
        formatted_output += f"\n{record_type} Records:\n"
        
        if isinstance(result, str):
            formatted_output += f"  {result}\n"
            continue
            
        if isinstance(result, list):
            for item in result:
                if record_type == 'A':
                    formatted_output += f"  {item.host}\n"
                elif record_type == 'AAAA':
                    formatted_output += f"  {item.host}\n"
                elif record_type == 'CNAME':
                    formatted_output += f"  {item.cname}\n"
                elif record_type == 'MX':
                    formatted_output += f"  Priority: {item.priority}, Host: {item.host}\n"
                elif record_type == 'NS':
                    formatted_output += f"  {item.host}\n"
                elif record_type == 'TXT':
                    formatted_output += f"  {item.text}\n"
                elif record_type == 'PTR':
                    formatted_output += f"  {item.name}\n"
        elif record_type == 'SOA':
            formatted_output += f"  Primary NS: {result.nsname}\n"
            formatted_output += f"  Hostmaster: {result.hostmaster}\n"
            formatted_output += f"  Serial: {result.serial}\n"
            formatted_output += f"  Refresh: {result.refresh}\n"
            formatted_output += f"  Retry: {result.retry}\n"
            formatted_output += f"  Expires: {result.expires}\n"
            formatted_output += f"  Minttl: {result.minttl}\n"
    
    return formatted_output

# 使用示例
async def main():
    domain = "github.com"
    formatted_results = await format_dns_results(domain)
    print(formatted_results)

if __name__ == "__main__":
    asyncio.run(main())