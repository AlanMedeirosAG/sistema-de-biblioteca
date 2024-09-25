from flask import Blueprint, request, jsonify
from model.estoque_model import create_estoque, get_estoque, update_estoque, delete_estoque

estoque_bp = Blueprint('estoque_bp', __name__)

@estoque_bp.route('/estoque', methods=['POST'])
def create_estoque_route():
    data = request.json
    create_estoque(data)
    return jsonify({"message": "estoque inserted successfully"}), 201

@estoque_bp.route('/estoque', methods=['GET'])
def get_estoque_route():
    estoque = get_estoque()
    return jsonify(estoque), 200

@estoque_bp.route('/estoque/<int:id>', methods=['PUT'])
def update_estoque_route(id):
    data = request.json
    update_estoque(id, data)
    return jsonify({"message": "estoque updated successfully"}), 200

@estoque_bp.route('/estoque/<int:id>', methods=['DELETE'])
def delete_estoque_route(id):
    delete_estoque(id)
    return jsonify({"message": "estoque deleted successfully"}), 200