import proxy_server

HOSTNAME = ''
PORT = 8080

print('Starting proxy server\n')
proxy = proxy_server.ProxyServer(HOSTNAME, PORT)
proxy.accept_requests()
print('Stopped proxy server')
