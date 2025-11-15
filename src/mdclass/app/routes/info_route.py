from flask import Blueprint, render_template

from mdclass.models.info import hyperparams, feature_importances
from mdclass.models import storage

info_route = Blueprint('info_route', __name__)


@info_route.route('/info', methods=['GET'])
def index():
    model = storage.load()

    return render_template(
        'info.j2',
        hyperparams=hyperparams(model).to_html(
            header=True, index=False, border=False
        ),
        feature_importances=feature_importances(model).to_html(
            header=True, index=False, border=False
        ),
        title='Modelo de Classificação de Transtornos Mentais',
    )
