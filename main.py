from flask import Flask
from server.routes import Routes
from api.sail_client import SAILClient

if __name__ == "__main__":
    flask_app = Flask(__name__)
    api_client = SAILClient()

    routes = Routes(flask_app, api_client)
    routes.configure()
    routes.run()
