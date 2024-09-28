from flask import Blueprint, request, jsonify
from model.usuario_model import create_usuario, get_usuarios, update_usuario, delete_usuario, get_usuario_login

usuario_bp = Blueprint('usuario_bp', __name__)

# Rota para criar um novo usuário (POST /usuario)
@usuario_bp.route('/usuario', methods=['POST'])
def create_usuario_route():
    data = request.json
    create_usuario(data)  # Chama a função que cria o usuário
    return jsonify({"message": "Usuário inserido com sucesso!"}), 201

# Rota para obter todos os usuários (GET /usuario)
@usuario_bp.route('/usuario', methods=['GET'])
def get_usuarios_route():
    usuarios = get_usuarios()
    return jsonify(usuarios), 200

# Rota para login de usuário (POST /login)
@usuario_bp.route('/login', methods=['POST'])
def get_usuario_login_route():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')
    
    usuario = get_usuario_login(email, senha)
    
    if usuario:
        return jsonify({"message": "Login bem-sucedido!", "usuario": usuario}), 200
    else:
        return jsonify({"message": "E-mail ou senha incorretos!"}), 401

# Rota para atualizar um usuário (PUT /usuario/<id>)
@usuario_bp.route('/usuario/<int:id>', methods=['PUT'])
def update_usuario_route(id):
    data = request.json
    update_usuario(id, data)
    return jsonify({"message": "Usuário atualizado com sucesso!"}), 200

# Rota para deletar um usuário (DELETE /usuario/<id>)
@usuario_bp.route('/usuario/<int:id>', methods=['DELETE'])
def delete_usuario_route(id):
    delete_usuario(id)
    return jsonify({"message": "Usuário deletado com sucesso!"}), 200

