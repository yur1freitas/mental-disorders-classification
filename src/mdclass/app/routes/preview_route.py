from typing import final

from flask import Blueprint, render_template, request
from wtforms import BooleanField, Form, IntegerField, SelectField
from wtforms.validators import NumberRange

from mdclass.models import storage
from mdclass.models.predict import (
    PredictInput,
    predict,
)

preview_route = Blueprint('preview_route', __name__)


@final
class ModelForm(Form):
    mood_swing = BooleanField(
        'Oscilações de Humor?',
        description='Sente que seu humor muda drasticamente muitas vezes',
    )
    suicidal_thoughts = BooleanField(
        'Pensamentos Suicidas?',
        description='Possui pensamentos que vizam tirar a própria vida',
    )
    anorxia = BooleanField(
        'Restrição Alimentar?',
        description='Tende a ser regido em sua alimentação ou pula muitas refeições',
    )
    authority_respect = BooleanField(
        'Respeito à Autoridade?',
        description='Tende a obdecer ou respeitar pessoas que possuem autoridade maior',
    )
    try_explanation = BooleanField(
        'Tentativa de Explicação?',
        description='Tende a explicar tudo o que acontence ao seu redor?',
    )
    aggressive_response = BooleanField(
        'Resposta Agressiva?',
        description='Tende a responder agressivamente sem motivo',
    )
    ignore_and_move_on = BooleanField(
        'Ignorar e Seguir em Frente?',
        description='Ignora os problemas e tenta seguir em frente',
    )
    nervous_break_down = BooleanField(
        'Colapso Nervoso?',
        description='Desiquilibrado físicamente e mentalmente, se sente incapaz em lidar com as pressões físicas e emocionais',
    )
    admit_mistakes = BooleanField(
        'Reconhece Erros?',
        description='Reconhece os próprios erros que cometeu',
    )
    overthinking = BooleanField(
        'Pensamento Excessivo?',
        description='Possui o hábito de pensar demais sobre situações do dia a dia ou eventos futuros',
    )
    sexual_activity = IntegerField(
        'Atividade Sexual',
        default=0,
        description='De uma escala de 0-10, como se sente em relação a sua atividade sexual',
        validators=[
            NumberRange(0, 10),
        ],
    )
    concentration = IntegerField(
        'Concentração',
        default=0,
        description='De uma escala de 0-10, como se sente em relação a sua capacidade de concentração',
        validators=[
            NumberRange(0, 10),
        ],
    )
    optimisim = IntegerField(
        'Otimismo',
        default=0,
        description='De uma escala de 0-10, como se sente em relação ao seu otimismo',
        validators=[
            NumberRange(0, 10),
        ],
    )
    sadness = SelectField(
        'Se sente Triste:',
        description='Com que frequência se sente triste?',
        choices=[
            ('seldom', 'Raramente'),
            ('sometimes', 'Às vezes'),
            ('usually', 'Normalmente'),
            ('most_often', 'Muitas vezes'),
        ],
    )
    euphoric = SelectField(
        'Se sente Euforico',
        description='Com que frequência se sente euforico?',
        choices=[
            ('seldom', 'Raramente'),
            ('sometimes', 'Às vezes'),
            ('usually', 'Normalmente'),
            ('most_often', 'Muitas vezes'),
        ],
    )
    exhausted = SelectField(
        'Se sente Exausto:',
        description='Com que frequência se sente exausto?',
        choices=[
            ('seldom', 'Raramente'),
            ('sometimes', 'Às vezes'),
            ('usually', 'Normalmente'),
            ('most_often', 'Muitas vezes'),
        ],
    )
    sleep_disorder = SelectField(
        'Diculdade para Dormir:',
        description='Com que frequência você sente dificuldade em dormir',
        choices=[
            ('seldom', 'Raramente'),
            ('sometimes', 'Às vezes'),
            ('usually', 'Normalmente'),
            ('most_often', 'Muitas vezes'),
        ],
    )


model = storage.load()


@preview_route.route('/preview', methods=['GET', 'POST'])
def preview():
    form = ModelForm(request.form)
    context: dict[str, str | None] = {
        'result': None,
    }

    if request.method == 'POST' and form.validate():
        params = PredictInput(**form.data)

        params.optimisim = params.optimisim / 10
        params.concentration = params.concentration / 10
        params.sexual_activity = params.sexual_activity / 10

        result = predict(model, params=params)
        context.update({'result': result.label})

    return render_template(
        'preview.j2',
        title='Model Preview',
        form=form,
        **context,
    )
