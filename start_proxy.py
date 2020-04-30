import subprocess
from multiprocessing import Process

from proxy_server.proxy_server import ProxyServer

HOSTNAME = ''
PORT = 8080


def run_db():
    subprocess.call(['python3', 'proxy_db/manage.py', 'runserver'])


def run_proxy():
    proxy = ProxyServer(HOSTNAME, PORT)
    proxy.accept_requests()


print('Started proxy server\n')
p1 = Process(target=run_db)
p2 = Process(target=run_proxy)
p1.start()
p2.start()
p1.join()
p2.join()
print('Stopped proxy server')
