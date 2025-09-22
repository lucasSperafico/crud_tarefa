from flask import Flask
<<<<<<< HEAD
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
=======
from .Hello.routes import hello_bp
from .models import db

def create_app():
    app =  Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///hello.db'
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///Tarefas.db'
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(hello_bp)
    
    return app 
>>>>>>> 696040a (CSS adicionado)
