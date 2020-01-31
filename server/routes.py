class Routes:
    """
    Configure the server routes for making queries, and uses the API client to
    obtain the results.
    """

    def __init__(self, flask_app, api_client):
        """
        :param Flask flask_app:
            An instance of the flask.
        
        :param SAILClient api_client:
            An instance of the API client.
        """
        self._flask_app = flask_app
        self._api_client = api_client

    def configure(self):
        """
        Configure the server routes.
        """
        self._configure_index()
        self._configure_questions()
        self._configure_answers()
        self._configure_comments()

    def run(self, debug=False):
        """
        Runs flask in development mode.
        
        :param bool debug:
            True to run in debug mode or False otherwise.
        """
        self._flask_app.run(debug=debug)

    def _configure_index(self):
        """
        Configures the home page.
        """

        @self._flask_app.route("/")
        def index():
            return self._flask_app.send_static_file("index.html")

    def _configure_questions(self, subpath="questions"):
        """
        Configures routes for querying questions.
        """

        @self._flask_app.route(f"/{subpath}/top_ten_last_week/<string:tag>")
        def top_ten_last_week(tag):
            return self._api_client.get_top_ten_questions_last_week(tag)

        @self._flask_app.route(f"/{subpath}/ten_newest/<string:tag>")
        def ten_newest(tag):
            return self._api_client.get_ten_newest_questions(tag)

    def _configure_answers(self, subpath="answers"):
        """
        Configures routes for querying answers.
        """

        @self._flask_app.route(f"/{subpath}/<int:question_id>")
        def answers(question_id):
            return self._api_client.get_answers(question_id)

    def _configure_comments(self, subpath="comments"):
        """
        Configures routes for querying comments.
        """

        @self._flask_app.route(f"/{subpath}/<int:post_id>")
        def comments(post_id):
            return self._api_client.get_comments(post_id)
