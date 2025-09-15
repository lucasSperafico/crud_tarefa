from flask import Flask
from .tarefas.routes import tarefa_bp
from .models import db

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
    
    db.init_app(app)    
    
    with app.app_context():
        db.create_all()

    app.register_blueprint(tarefa_bp)

    return app
