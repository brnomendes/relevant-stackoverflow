from api.client import Client


class StackOverflowClient:
    """
    """

    def __init__(self, key=None):
        self._key = key
        self._url = "https://api.stackexchange.com"
        self._site = "stackoverflow"
        self._client = Client()

    def get_questions(self, sort, order, tagged, size, from_date=None):
        """
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
        """
        params = self._get_default_params()
        params["pagesize"] = size
        params["order"] = order
        params["sort"] = sort

        result = self._client.get(f"{self._url}/posts/{post_id}/comments", params)
        return self._get_items(result)

    def _get_default_params(self):
        """
        """
        return {
            "filter": "withbody",
            "site": self._site,
            "key": self._key,
        }

    def _get_items(self, result):
        """
        """
        if result is not None and "items" in result:
            return result["items"]
        else:
            return list()


class SAILClient(StackOverflowClient):
    """
    """

    def get_ten_android_questions_last_week(self):
        """
        10 most voted Android-related questions that are created in the past
        week.
        """
        from datetime import datetime, timedelta

        last_week = datetime.today() - timedelta(days=7)
        result = self.get_questions(
            sort="votes",
            order="desc",
            tagged="android",
            size=10,
            from_date=int(last_week.timestamp()),
        )

        return result

    def get_ten_newest_questions(self):
        """
        10 newest Android-related questions
        """
        result = self.get_questions(
            sort="creation", order="desc", tagged="android", size=10,
        )
        return result
