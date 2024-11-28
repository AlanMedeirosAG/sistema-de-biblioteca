from flask import Blueprint, request, jsonify
from model.historico_model import create_historico, get_historico, update_historico, delete_historico

#blueprint
historico_bp = Blueprint('historico_bp', __name__)

# Rota para criar um novo historico (POST /historico)
@historico_bp.route('/historico', methods=['POST'])
def create_histotico_route():
    data = request.json
    create_historico(data)
    return jsonify({"message": "historico inserted successfully"}), 201

# Rota para obter um historico (GET /historico)
@historico_bp.route('/historico', methods=['GET'])
def get_histotico_route():
    historico = get_historico()
    return jsonify(historico), 200

# Rota para atualizar um historico (PUT /historico)
@historico_bp.route('/historico/<int:id>', methods=['PUT'])
def update_histotico_route(id):
    data = request.json
    update_historico(id, data)
    return jsonify({"message": "historico updated successfully"}), 200

# Rota para deletar um historico (DELETE /historico)
@historico_bp.route('/historico/<int:id>', methods=['DELETE'])
def delete_histotico_route(id):
    delete_historico(id)
    return jsonify({"message": "historico deleted successfully"}), 200
    
