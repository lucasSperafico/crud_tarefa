from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Tarefa, db

tarefa_bp = Blueprint('tarefa', __name__)

@tarefa_bp.route('/')
def index():
    tarefas = Tarefa.query.all()
    return render_template('index.html', tarefas=tarefas)

@tarefa_bp.route('/novaTarefa', methods=['POST'])
def nova_tarefa():
    descricao = request.form['descricao']
    nova = Tarefa(descricao=descricao)
    db.session.add(nova)
    db.session.commit()
    return redirect(url_for('tarefa.index'))

@tarefa_bp.route('/removerTarefa/<int:tarefa_id>', methods=['POST'])
def remover_tarefa(tarefa_id):
    tarefa = Tarefa.query.get(tarefa_id)
    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
    return redirect(url_for('tarefa.index'))

@tarefa_bp.route('/editarTarefa/<int:tarefa_id>', methods=['POST'])
def editar_tarefa(tarefa_id):
    tarefa = Tarefa.query.get(tarefa_id)
    if tarefa:
        tarefa.descricao = request.form['descricao']
        db.session.commit()
    return redirect(url_for('tarefa.index'))
