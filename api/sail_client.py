from api.stackoverflow import StackOverflowClient


class SAILClient(StackOverflowClient):
    """
    """

    def get_top_ten_questions_last_week(self, tag):
        """
        10 most voted tag-related questions that are created in the past
        week.
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
        10 newest Android-related questions
        """
        result = self.get_questions(sort="creation", order="desc", tagged=tag, size=10,)
        return result
