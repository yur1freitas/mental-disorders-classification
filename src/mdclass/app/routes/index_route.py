from flask import Blueprint, render_template

index_route = Blueprint('index_route', __name__)


@index_route.route('/', methods=['GET'])
def index():
    return render_template(
        'home.j2',
        title='Modelo de Classificação de Transtornos Mentais',
    )
