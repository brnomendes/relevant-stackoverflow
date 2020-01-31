from api.stackoverflow import StackOverflowClient


class SAILClient(StackOverflowClient):
    """
    A StackOverflow client with some pre-configured queries.
    """

    def get_top_ten_questions_last_week(self, tag):
        """
        Get the ten most voted tag-related questions that are created in the
        past week.
        
        :param str tag:
            Select questions that have this tag.
        
        :rtype dict("result": list):
        :returns:
            A dictionary with the query result.
        """
        from datetime import datetime, timedelta

        last_week = datetime.today() - timedelta(days=7)
        result = self.get_questions(
            sort="votes",
            order="desc",
            tagged=tag,
            size=10,
            from_date=int(last_week.timestamp()),
        )

        return result

    def get_ten_newest_questions(self, tag):
        """
        Get the ten newest tag-related questions.
        
        :param str tag:
            Select questions that have this tag.
        
        :rtype dict("result": list):
        :returns:
            A dictionary with the query result.
        """
        result = self.get_questions(sort="creation", order="desc", tagged=tag, size=10)
        return result
