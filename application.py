from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello from 740mo2tq Elastic Beanstalk CI-CD"
