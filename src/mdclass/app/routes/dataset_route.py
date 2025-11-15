from flask import Blueprint, render_template

from mdclass.data.loaders import load_raw_dataset

dataset_route = Blueprint('dataset_route', __name__)


@dataset_route.route('/dataset', methods=['GET'])
def dataset():
    df = load_raw_dataset()

    return render_template(
        'dataset.j2',
        title='Dataset de Sintomas de Transtornos Mentais',
        tables=[df.to_html(header=True, index=False, border=False)],
    )
