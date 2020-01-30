import requests


class Client:
    """
    """

    def _build_url(self, api_url, params):
        """
        """
        prepared = requests.Request("GET", api_url, params=params).prepare()
        return prepared.url

    def _get(self, url):
        """
        """
        try:
            response = requests.get(url)
        except ConnectionError:
            return None

        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get(self, api_url, params):
        """
        """
        url = self._build_url(api_url, params)
        return self._get(url)
