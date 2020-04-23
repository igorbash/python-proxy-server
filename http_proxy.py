import socket
import http.server
import http.client
import socketserver

from proxy_server_abstract import ProxyServerAbstract, MAX_REQUEST_LEN, CONNECTION_TIMEOUT, MAX_CONNECTIONS


class HTTPProxy(ProxyServerAbstract):
    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        self._handler = HTTPProxy.handle_request
        self._server_socket = socketserver.TCPServer((self._host, self._port), self._handler)

    def accept_requests(self):
        try:
            print("serving at port", self._port)
            self._server_socket.handle_request()
        except KeyboardInterrupt:
            print('Stopping server')
        finally:
            self._server_socket.server_close()

    @staticmethod
    def handle_request(request: socket.socket, client_address, self: socketserver.TCPServer):
        client_request = request.recv(MAX_REQUEST_LEN)
        (url, port) = HTTPProxy._get_url_and_port(client_request)
        server_connection = http.client.HTTPConnection(url, port)
        print(server_connection.request(client_request))
        request.close()
        self.server_close()
        pass
