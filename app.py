from flask import Flask
from flask_restful import Api
from routes import setup_routes
from dotenv import load_dotenv
from db import db

app = Flask(__name__)
load_dotenv(".env", verbose=True)
app.config.from_envvar("APPLICATION_SETTINGS")
api = Api(app)
db.init_app(app)


setup_routes(api)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
