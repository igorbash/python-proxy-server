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
