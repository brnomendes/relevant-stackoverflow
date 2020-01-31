import requests
from datetime import datetime


class Client:
    """
    HTTP client for GET request with a simple memory cache.
    """

    def __init__(self, cache_timeout=60):
        """
        :param float cache_timeout:
            The timeout to expire the response of a url in the cache.
        """
        self._cache_timeout = cache_timeout
        self._mem_cache = dict()

    def _build_url(self, api_url, params):
        """
        Build a url by adding query parameters to the end of the path.

        :param str api_url:
            The API query url.

        :param dict(str: str|list) params:
            A dictionary of parameters for the query.

        :rtype str:
        :returns:
            The built url.
        """
        prepared = requests.Request("GET", api_url, params=params).prepare()
        return prepared.url

    def _get(self, url):
        """
        Returns data from a url. If the data is valid in the cache, it returns
        from the cache, otherwise it makes a new GET request.

        If the GET fails, then try to return the last cache result even if it's
        invalidated by the timeout.

        :param str url:
            The url to do the GET.

        :rtype dict|None:
        :returns:
            The result from GET or from cache, if it was not possible to obtain
            returns None.
        """
        data = self._get_from_cache(url, force=False)
        if data:
            return data

        try:
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
        Get the result of an url in the memory cache.
        
        :param str url:
            The url to get the data from the cache.
        
        :param bool force:
            If true, the url timeout will be ignored and the latest data will be
            returned.
        
        :rtype dict|None:
        :returns:
            Returns the data from the cache or None otherwise.
        """
        if url not in self._mem_cache:
            return None

        diff_time = datetime.now().timestamp() - self._mem_cache[url]["time"]
        if force or diff_time <= self._cache_timeout:
            return self._mem_cache[url]["data"]

        return None

    def _set_in_cache(self, url, data):
        """
        Saves the data of a GET from a url to the cache.  
        
        :param str url:
            The url that the GET was made.
        
        :param dict data:
            The data obtained from the URL.
        """
        self._mem_cache[url] = dict()
        self._mem_cache[url]["data"] = data
        self._mem_cache[url]["time"] = datetime.now().timestamp()

    def get(self, api_url, params):
        """
        Try to get the data from the URL of a GET request or from the memory
        cache
        
        :param str api_url:
            The API query url.

        :param dict(str: str|list) params:
            A dictionary of parameters for the query.
            
        :rtype dict|None:
        :returns:
            The data obtained or None otherwise.
        """
        url = self._build_url(api_url, params)
        return self._get(url)
