import requests
from datetime import datetime


class Client:
    """
    """

    def __init__(self, cache_timeout=60):
        """
        """
        self._cache_timeout = cache_timeout
        self._mem_cache = dict()

    def _build_url(self, api_url, params):
        """
        """
        prepared = requests.Request("GET", api_url, params=params).prepare()
        return prepared.url

    def _get(self, url):
        """
        """
        data = self._get_from_cache(url, force=False)
        if data:
            return data

        try:
            print("request", url)
            response = requests.get(url)
        except Exception:
            return self._get_from_cache(url, force=True)

        if response.status_code == 200:
            data = response.json()
            self._set_in_cache(url, data)
            return data
        else:
            return self._get_from_cache(url, force=True)

    def _get_from_cache(self, url, force=False):
        """
        """
        if url not in self._mem_cache:
            return None

        diff_time = datetime.now().timestamp() - self._mem_cache[url]["time"]
        if force or diff_time <= self._cache_timeout:
            return self._mem_cache[url]["data"]

        return None

    def _set_in_cache(self, url, data):
        """
        """
        self._mem_cache[url] = dict()
        self._mem_cache[url]["data"] = data
        self._mem_cache[url]["time"] = datetime.now().timestamp()

    def get(self, api_url, params):
        """
        """
        url = self._build_url(api_url, params)
        return self._get(url)
