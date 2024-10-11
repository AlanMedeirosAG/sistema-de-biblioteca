from flask import Blueprint, request, jsonify
from model.usuario_model import create_usuario, get_usuarios, update_usuario, delete_usuario, get_usuario_login

usuario_bp = Blueprint('usuario_bp', __name__)

# Rota para criar um novo usuário (POST /usuario)
@usuario_bp.route('/usuario', methods=['POST'])
def create_usuario_route():
    try:
        data = request.json
        # Validação dos dados
        if not data or 'nome' not in data or 'email' not in data or 'senha' not in data or 'tipo_usuario' not in data:
            return jsonify({"message": "Campos 'nome', 'email', 'senha' e 'tipo_usuario' são obrigatórios."}), 400

        # Chame uma função única que insere no banco de dados
        create_usuario(data)  
        
        return jsonify({"message": "Usuário inserido com sucesso!"}), 201
    
    except Exception as e:
        return jsonify({"message": f"Erro ao inserir usuário: {str(e)}"}), 500


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
        return jsonify({
            "message": "Login bem-sucedido!",
            "usuario": {
                "email": usuario['email'],
                "tipo": usuario['tipo']  
            }
        }), 200
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

