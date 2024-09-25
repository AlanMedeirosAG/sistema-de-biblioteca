from flask import Blueprint, request, jsonify
from model.usuario_model import create_usuario, get_usuarios, update_usuario, delete_usuario

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/usuario', methods=['POST'])
def create_usuario_route():
    data = request.json
    create_usuario(data)
    return jsonify({"message": "usuario inserted successfully"}), 201

@usuario_bp.route('/usuario', methods=['GET'])
def get_usuario_route():
    usuarios = get_usuarios()
    return jsonify(usuarios), 200

@usuario_bp.route('/usuario/<int:id>', methods=['PUT'])
def update_usuario_route(id):
    data = request.json
    update_usuario(id, data)
    return jsonify({"message": "usuario updated successfully"}), 200

@usuario_bp.route('/usuario/<int:id>', methods=['DELETE'])
def delete_usuario_route(id):
    delete_usuario(id)
    return jsonify({"message": "usuario deleted successfully"}), 200
