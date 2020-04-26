from proxy_server.proxy_server import ProxyServer
HOSTNAME = ''
PORT = 8080

proxy = ProxyServer(HOSTNAME, PORT)
print('Started proxy server\n')
proxy.accept_requests()
print('Stopped proxy server')
