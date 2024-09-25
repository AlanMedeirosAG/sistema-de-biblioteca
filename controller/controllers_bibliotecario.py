from flask import Blueprint, request, jsonify
from model.bibliotecario_model import create_bibliotecario, get_bibliotecarios, update_bibliotecario, delete_bibliotecario

bibliotecario_bp = Blueprint('bibliotecario_bp', __name__)

@bibliotecario_bp.route('/bibliotecario', methods=['POST'])
def create_usuario_route():
    data = request.json
    create_bibliotecario(data)
    return jsonify({"message": "bibliotecario inserted successfully"}), 201

@bibliotecario_bp.route('/bibliotecario', methods=['GET'])
def get_usuario_route():
    bibliotecarios = get_bibliotecarios()
    return jsonify(bibliotecarios), 200

@bibliotecario_bp.route('/bibliotecario/<int:id>', methods=['PUT'])
def update_usuario_route(id):
    data = request.json
    update_bibliotecario(id, data)
    return jsonify({"message": "bibliotecario updated successfully"}), 200

@bibliotecario_bp.route('/bibliotecario/<int:id>', methods=['DELETE'])
def delete_usuario_route(id):
    delete_bibliotecario(id)
    return jsonify({"message": "bibliotecario deleted successfully"}), 200