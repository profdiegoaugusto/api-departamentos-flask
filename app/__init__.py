from flask import Flask


def create_app():
    """Cria e configura uma instância do aplicativo Flask."""

    app = Flask(__name__)

    # Registra os blueprints (classes de controle)

    return app
