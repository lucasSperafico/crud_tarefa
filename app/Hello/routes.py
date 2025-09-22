from flask import Blueprint, render_template, request, redirect, url_for
from ..models import User, Tarefas, db

hello_bp = Blueprint("hello", __name__)

@hello_bp.route('/')
def index():
    usuarios = User.query.all()
    return render_template('index.html', usuarios=usuarios)

@hello_bp.route('/novoUsuario', methods=['POST'])
def novoUsuario():
    nome_usuario = request.form['nome_usuario']
    novo_usuario = User(username=nome_usuario)
    db.session.add(novo_usuario)
    db.session.commit()
    return redirect(url_for('hello.index'))

@hello_bp.route('/removerUsuario/<int:usuario_id>', methods=['POST'])
def removerUsuario(usuario_id):
    usuario = User.query.get(usuario_id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
    return redirect(url_for('hello.index'))

@hello_bp.route('/editarUsuario/<int:usuario_id>', methods=['POST'])
def editarUsuario(usuario_id):
    usuario = User.query.get(usuario_id)
    if usuario:
        usuario.username = request.form['nome_usuario']
        db.session.commit()
    return redirect(url_for('hello.index'))

@hello_bp.route('/tarefas', methods=['GET', 'POST'])
def tarefas():
    if request.method == 'POST':
        tarefa_desc = request.form['descricao']
        nova_tarefa = Tarefas(descricao=tarefa_desc)
        db.session.add(nova_tarefa)
        db.session.commit()
        return redirect(url_for('hello.tarefas'))

    todas_tarefas = Tarefas.query.all()
    return render_template('tarefas.html', tarefas=todas_tarefas)

@hello_bp.route('/editarTarefa/<int:tarefa_id>', methods=['POST'])
def editarTarefa(tarefa_id):
    tarefa = Tarefas.query.get(tarefa_id)
    if tarefa:
        tarefa.descricao = request.form['descricao']
        db.session.commit()
    return redirect(url_for('hello.tarefas'))

@hello_bp.route('/removerTarefa/<int:tarefa_id>', methods=['POST'])
def removerTarefa(tarefa_id):
    tarefa = Tarefas.query.get(tarefa_id)
    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
    return redirect(url_for('hello.tarefas'))

@hello_bp.route('/sobre')
def sobre():
    return render_template('sobre.html')