from flask import Blueprint, request, jsonify
from model.historico_model import create_historico, get_historico, update_historico, delete_historico

historico_bp = Blueprint('historico_bp', __name__)

@historico_bp.route('/historico', methods=['POST'])
def create_histotico_route():
    data = request.json
    create_historico(data)
    return jsonify({"message": "historico inserted successfully"}), 201

@historico_bp.route('/historico_bp', methods=['GET'])
def get_histotico_route():
    historico = get_historico()
    return jsonify(historico), 200

@historico_bp.route('/historico/<int:id>', methods=['PUT'])
def update_histotico_route(id):
    data = request.json
    update_historico(id, data)
    return jsonify({"message": "historico updated successfully"}), 200

@historico_bp.route('/historico/<int:id>', methods=['DELETE'])
def delete_histotico_route(id):
    delete_historico(id)
    return jsonify({"message": "historico deleted successfully"}), 200