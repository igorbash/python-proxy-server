import socket
from threading import Thread

from proxy_server_abstract import ProxyServerAbstract, CONNECTION_TIMEOUT, MAX_CONNECTIONS, MAX_REQUEST_LEN
from http_headers import HttpHeaders


class ProxyServer(ProxyServerAbstract):
    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        with open('domains_blacklist') as blacklist:
            self._blacklist = blacklist.readlines()
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
                client_thread = Thread(name=client_address, target=self._handle_request,
                                       args=(client_connection, client_address))
                client_thread.setDaemon(True)
                client_thread.start()
        except KeyboardInterrupt:
            print("Stopping server")
        finally:
            self.__server_socket.close()

    def _handle_request(self, client_connection: socket.socket, client_address):
        try:
            request = client_connection.recv(MAX_REQUEST_LEN)
            headers = HttpHeaders(request)
            (hostname, port) = headers.get_host_name_and_port()
            for domain in self._blacklist:
                if hostname.decode() in domain:
                    ProxyServer._handle_blacklist_request(client_connection)
                    break
            else:
                ProxyServer._handle_original_request(client_connection, headers, hostname, port)

        except KeyboardInterrupt:
            print("Stopping connection to client")
        finally:
            client_connection.close()
            print(f'Done client {client_address} request\n')

    @staticmethod
    def _handle_original_request(client_connection: socket.socket, headers: HttpHeaders, hostname, port):
        try:
            headers.change_user_agent()
            server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_connection.settimeout(CONNECTION_TIMEOUT)
            server_connection.connect((hostname, port))
            print(f'Connected to server: {hostname.decode()} on port: {port}')

            ProxyServer._send_data_to_server(server_connection, headers.create_raw_request())
            ProxyServer._receive_and_send_data_to_client(server_connection, client_connection)
        except KeyboardInterrupt:
            print(f'Closing connection to server: {hostname.decode()} on port: {port}')
        finally:
            server_connection.close()

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

    @staticmethod
    def _handle_blacklist_request(client_connection: socket.socket):
        client_connection.send(b'HTTP/1.0 200 OK\n')
        client_connection.send(b'Content-Type: text/html\n')
        client_connection.send(b'\n')
        with open('human_rights.html') as human_rights_page:
            for line in human_rights_page.readlines():
                client_connection.send(line.encode())
