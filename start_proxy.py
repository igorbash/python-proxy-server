import proxy_server
import http_proxy

HOSTNAME = ''
PORT = 8080

# proxy_type = int(input('1 for http 2 for not http: '))
proxy_type = 2
proxy = None
if proxy_type == 1:
    proxy = http_proxy.HTTPProxy(HOSTNAME, PORT)
elif proxy_type == 2:
    proxy = proxy_server.ProxyServer(HOSTNAME, PORT)
else:
    exit(1)

print('Started proxy server\n')
proxy.accept_requests()
print('Stopped proxy server')
