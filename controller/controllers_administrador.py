from flask import Blueprint, request, jsonify
from model.administrador_model import create_administrador, get_administradores, update_administrador, delete_administrador

#blueprint
administrador_bp = Blueprint('administrador_bp', __name__)

# Rota para criar um novo administrador (POST /administrador)
@administrador_bp.route('/administrador', methods=['POST'])
def create_administrador_route():
    data = request.json
    create_administrador(data)
    return jsonify({"message": "administrador inserted successfully"}), 201

# Rota para obter um administrador (GET /administrador)
@administrador_bp.route('/administrador', methods=['GET'])
def get_administrador_route():
    usuarios = get_administradores()
    return jsonify(usuarios), 200

# Rota para atualizar um administrador (PUT /administrador)
@administrador_bp.route('/administrador/<int:id>', methods=['PUT'])
def update_administrador_route(id):
    data = request.json
    update_administrador(id, data)
    return jsonify({"message": "administrador updated successfully"}), 200

# Rota para deletar novo administrador (DELETE /administrador)
@administrador_bp.route('/administrador/<int:id>', methods=['DELETE'])
def delete_administrador_route(id):
    delete_administrador(id)
    return jsonify({"message": "administrador deleted successfully"}), 200