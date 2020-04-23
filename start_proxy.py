import proxy_server

HOSTNAME = ''
PORT = 8080

proxy = proxy_server.ProxyServer(HOSTNAME, PORT)
print('Started proxy server\n')
proxy.accept_requests()
print('Stopped proxy server')
