import requests


class ProxyDbUtils:
    def __init__(self, base_url=None):
        self._base_url = base_url or 'http://127.0.0.1:8000/'
        self._clients_url = base_url + 'clients/'
        self._cookies_url = base_url + 'cookies/'
        self._credentials_url = base_url + 'credentials/'

    def get_clients(self):
        response = requests.get(url=self._clients_url)
        if response.status_code == 200:
            return response.json()['results']
        return None

    def get_client_by_ip(self, ip: str):
        response = requests.get(url=self._clients_url + ip)
        if response.status_code == 200:
            return response.json()
        return None

    def add_client(self, client_ip: str):
        client = {'ip': client_ip}
        response = requests.post(url=self._clients_url, data=client)
        return response.status_code == 201

    def get_cookies(self):
        response = requests.get(url=self._cookies_url)
        if response.status_code == 200:
            return response.json()['results']
        return None

    def add_cookie(self, client_ip: str, cookie: str, host: str):
        cookie_json = {
            'user_ip': client_ip,
            'cookie': cookie,
            'host': host
        }
        response = requests.post(url=self._cookies_url, data=cookie_json)
        return response.status_code == 201

    def get_credentials(self):
        response = requests.get(url=self._credentials_url)
        if response.status_code == 200:
            return response.json()['results']
        return None

    def add_credential(self, client_ip, credential, host):
        credential_json = {
            'user_ip': client_ip,
            'cookie': credential,
            'host': host
        }
        response = requests.post(url=self._credentials_url, data=credential_json)
        return response.status_code == 201
