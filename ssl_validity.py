import ssl
import socket
from datetime import datetime

def check_remote_ssl_validity(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            expire_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            print(f"Certificate for {hostname} expires on {expire_date}")
            return expire_date > datetime.now()

# Example
check_remote_ssl_validity('example.com')