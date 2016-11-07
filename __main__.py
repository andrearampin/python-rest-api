from flask import Flask
from api import apis


""" Load application and register APIs Blueprint """
app = Flask(__name__)
app.register_blueprint(apis)


if __name__ == "__main__":
    app.run()