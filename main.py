import os
from flask import Flask
from flask_restful import Resource, Api
# from application.config import conf
from applications.config import LocalDevelopmentConfig
from applications.database import db

app = None


def create_app():
    app = Flask(__name__, template_folder="Templates")
    if os.getenv('ENV', "development") == "production":
      raise Exception("Currently no production config is setup.")
    else:
      print("Staring Local Development")
      app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()  
    return app


app = create_app()
app.secret_key="123456789"

from applications.controllers import *


if __name__ == '__main__':
  # Run the Flask app
  app.run(debug=True)
