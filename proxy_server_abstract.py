from abc import ABC, abstractmethod, ABCMeta
import socket

MAX_CONNECTIONS = 10
MAX_REQUEST_LEN = 4096
CONNECTION_TIMEOUT = 10


class ProxyServerMeta(ABCMeta):
    _instance = None

    def __call__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__call__(*args)
        return cls._instance


class ProxyServerAbstract(ABC, metaclass=ProxyServerMeta):
    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port

    @abstractmethod
    def accept_requests(self):
        pass

    @staticmethod
    def _get_url_and_port(request: bytes):
        # TODO: get specific port - if not only http
        url = request.split(b'\n\r\n')[0].split(b' ')[1]
        url = url[url.find(b'://') + 3:len(url) - 1]
        port = 80
        return url, port
