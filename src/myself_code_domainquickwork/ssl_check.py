import ssl
import socket
from datetime import datetime
import OpenSSL

def get_ssl_certificate_info(domain):
    # 尝试连接 HTTPS 端口
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            # 获取证书并转换成 OpenSSL 对象
            cert = ssock.getpeercert(True)
            x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, cert)
            
            # 获取证书详细信息
            cert_info = {
                "Issuer": x509.get_issuer().CN,
                "Subject": x509.get_subject().CN,
                "Start Date": datetime.strptime(x509.get_notBefore().decode(), "%Y%m%d%H%M%SZ"),
                "End Date": datetime.strptime(x509.get_notAfter().decode(), "%Y%m%d%H%M%SZ"),
                "Serial Number": x509.get_serial_number(),
            }
            return cert_info

domain = "www.bilibili.com"
try:
    cert_info = get_ssl_certificate_info(domain)
    print(f"SSL Certificate for {domain}:")
    print(cert_info)
except Exception as e:
    print(f"Failed to retrieve SSL certificate for {domain}: {e}")
