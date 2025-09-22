from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

<<<<<<< HEAD
class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(120), unique=True, nullable=False)
=======
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable= False)


class Tarefas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), unique=True, nullable=False)
>>>>>>> 696040a (CSS adicionado)
