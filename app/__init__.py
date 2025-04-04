from flask import Flask
from app.routes import api_bp  # Importa as rotas

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp)  # Registra as rotas
    return app
