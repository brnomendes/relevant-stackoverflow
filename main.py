from flask import Flask
from server.routes import Routes
from api.sail_client import SAILClient

flask_app = Flask(__name__)

api_client = SAILClient()
routes = Routes(flask_app, api_client)
routes.configure()

if __name__ == "__main__":
    routes.run()
