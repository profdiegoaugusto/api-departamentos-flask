from flask import Flask

from app.database import db_session, init_db


def create_app():
    """Cria e configura uma instância do aplicativo Flask."""

    app = Flask(__name__)

    @app.teardown_appcontext
    def encerrar_sessao(exception=None):
        db_session.remove()

    init_db()



    # Registra os blueprints (classes de controle)

    return app
