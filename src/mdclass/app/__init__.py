from flask import Flask

from mdclass.app import routes

_STATIC_FOLDER = 'static'
_TEMPLATE_FOLDER = 'templates'


def create_app() -> Flask:
    app = Flask(
        __name__,
        static_folder=_STATIC_FOLDER,
        template_folder=_TEMPLATE_FOLDER,
    )

    routes.register(app)

    return app
