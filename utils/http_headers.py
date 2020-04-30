import random


class HttpHeaders:
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 '
        'Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
        'CriOS/81.0.4044.124 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile '
        'Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
        'FxiOS/24.0 Mobile/15E148 Safari/605.1.15',
        'Mozilla/5.0 (Android 10; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0'
    ]

    def __init__(self, raw_request: bytes):
        str_request = raw_request.decode()
        fields = str_request.splitlines()
        self._http_request_type = fields[0]
        fields = fields[1:]
        self._http_headers = {k: v.strip() for k, v in [line.split(":", 1) for line in fields if ":" in line]}

    @property
    def http_request_type(self):
        return self._http_request_type

    @property
    def http_headers(self):
        return self._http_headers

    def create_raw_request(self):
        raw_request = self._http_request_type.encode() + b'\r\n'
        for k, v in self._http_headers.items():
            raw_request += k.encode() + b': ' + v.encode() + b'\r\n'
        return raw_request + b'\r\n'

    def change_user_agent(self):
        user_agent_to_change_to = random.choice(HttpHeaders.user_agents)
        self._http_headers['User-Agent'] = user_agent_to_change_to

    def get_host_name_and_port(self):
        hostname_port = self._http_headers['Host'].split(':')
        if len(hostname_port) == 1:
            return hostname_port[0].encode(), 80
        return hostname_port[0].encode(), int(hostname_port[1])

    def get_host(self):
        return self.get_host_name_and_port()[0]

    def get_cookies(self):
        if 'cookies' not in self._http_headers:
            return []
        cookies = self._http_headers['cookie'].split(';')
        return list(map(lambda c: c.split('='), cookies))

    def get_credentials(self):
        if 'Authorization' not in self._http_headers:
            return []
        return self._http_headers['Authorization'].split()
