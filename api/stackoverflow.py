from api.client import Client


class StackOverflowClient:
    """
    A client to query data on the StackOverflow API.
    """

    def __init__(self):
        self._key = self._get_stack_key()
        self._url = "https://api.stackexchange.com"
        self._site = "stackoverflow"
        self._client = Client()

    def _get_stack_key(self):
        """
        Try to get the stack overflow API key from the environment variables.
        
        :rtype str|None:
        :returns:
            User API key or None otherwise.
        """
        try:
            import os

            return os.environ["STACK_KEY"]
        except KeyError:
            return None

    def get_questions(self, sort, order, tagged, size, from_date=None):
        """
        Get the questions from the StackOverflow API.
        
        :rtype dict("result": list):
        :returns:
            A dictionary with the query result.
        """
        params = self._get_default_params()
        params["pagesize"] = size
        params["order"] = order
        params["sort"] = sort
        params["tagged"] = tagged
        params["fromdate"] = from_date

        result = self._client.get(f"{self._url}/questions", params)
        return self._get_items(result)

    def get_answers(self, question_id, size=100, order="desc", sort="votes"):
        """
        Get the answers from the StackOverflow API.
        
        :rtype dict("result": list):
        :returns:
            A dictionary with the query result.
        """
        params = self._get_default_params()
        params["pagesize"] = size
        params["order"] = order
        params["sort"] = sort

        result = self._client.get(
            f"{self._url}/questions/{question_id}/answers", params
        )
        return self._get_items(result)

    def get_comments(self, post_id, size=100, order="desc", sort="creation"):
        """
        Get the comments from the StackOverflow API.
        
        :rtype dict("result": list):
        :returns:
            A dictionary with the query result.
        """
        params = self._get_default_params()
        params["pagesize"] = size
        params["order"] = order
        params["sort"] = sort

        result = self._client.get(f"{self._url}/posts/{post_id}/comments", params)
        return self._get_items(result)

    def _get_default_params(self):
        """
        :rtype dict:
        :returns:
            Get parameters used by default in all queries.
        """
        return {
            "filter": "withbody",
            "site": self._site,
            "key": self._key,
        }

    def _get_items(self, result):
        """
        :rtype dict("result": list):
        :returns:
            Get query result data from the StackOverflow API.
        """
        if result is not None and "items" in result:
            return {"result": result["items"]}
        else:
            return {"result": list()}
