from flask import Blueprint, request, jsonify
from model.livro_model import create_livro, get_livros, update_livro, delete_livro,pesquisaLivro

#blueprint
livro_bp = Blueprint('livro_bp', __name__)

# Rota para criar um novo livro (POST /livro)
@livro_bp.route('/livro', methods=['POST'])
def create_livro_route():
    data = request.json
    create_livro(data)
    return jsonify({"message": "Livro inserted successfully"}), 201

# Rota para obter um livro (GET /livro)
@livro_bp.route('/livro', methods=['GET'])
def get_livros_route():
    livros = get_livros()
    return jsonify(livros), 200

# Rota para obter um livro atraves da pesquisa (GET /livro)
@livro_bp.route('/livro', methods=['GET'])
def get_pesquisa_livro():

    titulo = request.args.get('titulo')
    idlivro = request.args.get('idlivro')
    resultado = pesquisaLivro(titulo=titulo,idlivro=idlivro)

    if resultado:
        return jsonify(resultado), 200
    else:
        return jsonify({"mensagem": "Livro não encontrado"}), 404

# Rota para atualizar um livro (PUT /livro)
@livro_bp.route('/livro/<int:id>', methods=['PUT'])
def update_livro_route(id):
    data = request.json
    update_livro(id, data)
    return jsonify({"message": "Livro updated successfully"}), 200

# Rota para deletar um livro (DELETE /livro)
@livro_bp.route('/livro/<int:id>', methods=['DELETE'])
def delete_livro_route(id):
    delete_livro(id)
    return jsonify({"message": "Livro deleted successfully"}), 200
