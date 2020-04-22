import socket
from threading import Thread

MAX_CONNECTIONS = 10
MAX_REQUEST_LEN = 4096
CONNECTION_TIMEOUT = 10


# TODO: handle failures
# TODO: add prints
# TODO: make singleton
class ProxyServer:
    def __init__(self, host: str, port: int):
        self.__host = host
        self.__port = port
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__server_socket.bind((self.__host, self.__port))
        self.__server_socket.listen(MAX_CONNECTIONS)
        print(f'Proxy Server Listening on port {self.__port}...\n')

    def __del__(self):
        self.__server_socket.close()

    def accept_requests(self):
        try:
            while True:
                (client_connection, client_address) = self.__server_socket.accept()
                print(f'Connection accepted from: {client_address}')
                client_thread = Thread(name=client_address, target=ProxyServer.make_request,
                                       args=(client_connection, client_address))
                client_thread.setDaemon(True)
                client_thread.start()
        except KeyboardInterrupt:
            self.__server_socket.close()

    @staticmethod
    def make_request(client_connection: socket.socket, client_address):
        request = client_connection.recv(MAX_REQUEST_LEN)

        (url, port) = ProxyServer.__get_url_and_port(request)

        server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_connection.settimeout(CONNECTION_TIMEOUT)
        server_connection.connect((url, port))
        print(f'Connected to server: {url.decode()} on port: {port}')

        ProxyServer.__send_data_to_server(server_connection, request)
        ProxyServer.__receive_and_send_data_to_client(server_connection, client_connection)
        server_connection.close()
        client_connection.close()

        print(f'Done client {client_address} request\n')

    @staticmethod
    def __get_url_and_port(request: bytes):
        # TODO: get specific port - if not only http
        url = request.split(b'\n\r\n')[0].split(b' ')[1]
        url = url[url.find(b'://') + 3:len(url)-1]
        port = 80
        return url, port

    @staticmethod
    def __send_data_to_server(server_connection: socket.socket, request: bytes):
        server_connection.sendall(request)
        return server_connection

    @staticmethod
    def __receive_and_send_data_to_client(server_connection: socket.socket, client_connection: socket.socket):
        while True:
            try:
                data = server_connection.recv(MAX_REQUEST_LEN)
                if len(data) > 0:
                    client_connection.sendall(data)
                else:
                    break
            except socket.timeout:
                break
