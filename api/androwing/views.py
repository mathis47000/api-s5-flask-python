from flask import Flask
from androwing.database import db_session

app = Flask(__name__)

from .services import training, user

app.register_blueprint(training.bp)
app.register_blueprint(user.bp)

@app.route('/')
def menu():
    return "Welcome to androwing api"

@app.errorhandler(404)
def resource_not_found(e):
    return {"error": "Not found", "code": 404}, 404

@app.errorhandler(500)
def resource_not_found(e):
    return {"error": "Internal Server Error", "code": 500}, 500

@app.errorhandler(400)
def resource_not_found(e):
    return {"error": "Bad Request", "code": 400}, 400

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()