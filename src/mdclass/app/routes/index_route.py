from datetime import datetime

from flask import Blueprint, render_template

index_route = Blueprint('index_route', __name__)


@index_route.route('/', methods=['GET'])
def index():
    return render_template(
        'home.j2',
        year=datetime.now().year,
        title='Modelo de Classificação de Transtornos Mentais',
    )
