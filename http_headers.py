from email import message_from_string


class HttpHeaders:
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
