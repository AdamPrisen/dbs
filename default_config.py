import os

Debug = True
SECRET_KEY = os.environ["APP_SECRET_KEY"]
SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ['DB_USERNAME']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
SQLALCHEMY_TRACK_MODIFICATIONS = False