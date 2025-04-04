from flask import Blueprint, request, jsonify
from app.services import buscar_operadoras

api_bp = Blueprint("api", __name__)  # Cria um grupo de rotas

@api_bp.route("/buscar", methods=["GET"])
def buscar():
    termo = request.args.get("termo", "").lower()
    resultado = buscar_operadoras(termo)
    return jsonify(resultado)
