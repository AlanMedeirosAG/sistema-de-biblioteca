from flask import Blueprint, request, jsonify
from model.bibliotecario_model import create_bibliotecario, get_bibliotecarios, update_bibliotecario,get_bibliotecario_login , delete_bibliotecario

bibliotecario_bp = Blueprint('bibliotecario_bp', __name__)

@bibliotecario_bp.route('/bibliotecario', methods=['POST'])
def create_bibliotecario_route():
    data = request.json
    create_bibliotecario(data)
    return jsonify({"message": "bibliotecario inserted successfully"}), 201


# Rota para criar um novo bibliotecario (POST /bibliotecario)
@bibliotecario_bp.route('/bibliotecario', methods=['POST'])
def create_bibliotecario_login_route():
    try:
        data = request.json
        # Validação dos dados
        if 'senha' not in data:
            return jsonify({"message": "Campo é 'senha' é obrigatório."}), 400

        create_bibliotecario(data)  # Assumindo que sua função já faz as verificações necessárias
        # Retorno de sucesso
        return jsonify({"message": "bibliotecario inserido com sucesso!"}), 201
    
    except Exception as e:
        # Tratamento genérico de erros, pode incluir logs aqui
        return jsonify({"message": f"Erro ao inserir usuário: {str(e)}"}), 500

@bibliotecario_bp.route('/bibliotecario', methods=['GET'])
def get_bibliotecario_route():
    bibliotecarios = get_bibliotecarios()
    return jsonify(bibliotecarios), 200

@bibliotecario_bp.route('/login_bibliotecario', methods=['POST'])
def get_bibliotecario_login_route():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')
    
    bibliotecario = get_bibliotecario_login(email, senha)
    
    if bibliotecario:
        return jsonify({"message": "Login bem-sucedido!", "bibliotecario": bibliotecario}), 200
    else:
        return jsonify({"message": "E-mail ou senha incorretos!"}), 401

@bibliotecario_bp.route('/bibliotecario/<int:id>', methods=['PUT'])
def update_usuario_route(id):
    data = request.json
    update_bibliotecario(id, data)
    return jsonify({"message": "bibliotecario updated successfully"}), 200

@bibliotecario_bp.route('/bibliotecario/<int:id>', methods=['DELETE'])
def delete_bibliotecario_route(id):
    delete_bibliotecario(id)
    return jsonify({"message": "bibliotecario deleted successfully"}), 200
