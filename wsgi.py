from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/ready")
def ready():
    return "I am ready!\n"

@application.route("/health")
def ready():
    return "I am healthy!\n"

if __name__ == "__main__":
    application.run()
