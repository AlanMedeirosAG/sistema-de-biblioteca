from flask import Blueprint, request, jsonify
from model.administrador_model import create_administrador, get_administradores, update_administrador, delete_administrador

administrador_bp = Blueprint('administrador_bp', __name__)

@administrador_bp.route('/administrador', methods=['POST'])
def create_administrador_route():
    data = request.json
    create_administrador(data)
    return jsonify({"message": "administrador inserted successfully"}), 201

@administrador_bp.route('/administrador', methods=['GET'])
def get_administrador_route():
    usuarios = get_administradores()
    return jsonify(usuarios), 200

@administrador_bp.route('/administrador/<int:id>', methods=['PUT'])
def update_administrador_route(id):
    data = request.json
    update_administrador(id, data)
    return jsonify({"message": "administrador updated successfully"}), 200

@administrador_bp.route('/administrador/<int:id>', methods=['DELETE'])
def delete_administrador_route(id):
    delete_administrador(id)
    return jsonify({"message": "administrador deleted successfully"}), 200