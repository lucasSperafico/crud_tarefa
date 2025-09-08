from flask import Blueprint, render_template

hello_bp = Blueprint('hello', __name__)
name_bp = Blueprint('name', __name__)


@hello_bp.route('/')
def index():
    usuarios = ['Gabriel', 'Peterson pinto pequeno', 'Elano do gremio', 'Gabriel gadens']
    return render_template('index.html', usuarios=usuarios)

    
@name_bp.route('/sobre')
def index():
    return "Ola, [Seu Nome]! kkkkk"