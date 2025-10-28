from flask import Flask

from .info_route import info_route
from .index_route import index_route
from .preview_route import preview_route
from .dataset_route import dataset_route


def register(app: Flask) -> None:
    app.register_blueprint(index_route)
    app.register_blueprint(preview_route)
    app.register_blueprint(dataset_route)
    app.register_blueprint(info_route)


__all__ = ['register']
