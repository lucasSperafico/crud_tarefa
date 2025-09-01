from flask import Flask
from.hello.routes import hello_bp
from.hello.routes import name_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(hello_bp)
    app.register_blueprint(name_bp)

    return app