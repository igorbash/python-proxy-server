import socket
from threading import Thread

from proxy_server_abstract import ProxyServerAbstract, CONNECTION_TIMEOUT, MAX_CONNECTIONS, MAX_REQUEST_LEN


# TODO: handle failures
class ProxyServer(ProxyServerAbstract):
    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__server_socket.bind((self._host, self._port))
        self.__server_socket.listen(MAX_CONNECTIONS)
        print(f'Proxy Server Listening on port {self._port}...\n')

    def accept_requests(self):
        try:
            while True:
                (client_connection, client_address) = self.__server_socket.accept()
                print(f'Connection accepted from: {client_address}')
                client_thread = Thread(name=client_address, target=ProxyServer._make_request,
                                       args=(client_connection, client_address))
                client_thread.setDaemon(True)
                client_thread.start()
        except KeyboardInterrupt:
            print("Stopping server")
        finally:
            self.__server_socket.close()

    @staticmethod
    def _make_request(client_connection: socket.socket, client_address):
        request = client_connection.recv(MAX_REQUEST_LEN)

        (url, port) = ProxyServer._get_url_and_port(request)

        server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_connection.settimeout(CONNECTION_TIMEOUT)
        server_connection.connect((url, port))
        print(f'Connected to server: {url.decode()} on port: {port}')

        ProxyServer._send_data_to_server(server_connection, request)
        ProxyServer._receive_and_send_data_to_client(server_connection, client_connection)
        server_connection.close()
        client_connection.close()

        print(f'Done client {client_address} request\n')

    @staticmethod
    def _send_data_to_server(server_connection: socket.socket, request: bytes):
        server_connection.sendall(request)
        return server_connection

    @staticmethod
    def _receive_and_send_data_to_client(server_connection: socket.socket, client_connection: socket.socket):
        while True:
            try:
                data = server_connection.recv(MAX_REQUEST_LEN)
                if len(data) > 0:
                    client_connection.sendall(data)
                else:
                    break
            except socket.timeout:
                break
