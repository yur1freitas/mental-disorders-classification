from flask import Flask

from .dataset_route import dataset_route
from .preview_route import preview_route
from .index_route import index_route
from .info_route import info_route


def register(app: Flask) -> None:
    """Função responsável por registrar todas as rotas do site

    Args:
        app (Flask): Aplicação que deseja registrar as rotas
    """

    app.register_blueprint(index_route)
    app.register_blueprint(preview_route)
    app.register_blueprint(dataset_route)
    app.register_blueprint(info_route)


__all__ = ['register']
