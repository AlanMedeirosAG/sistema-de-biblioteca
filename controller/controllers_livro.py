from flask import Blueprint, request, jsonify
from model.livro_model import create_livro, get_livros, update_livro, delete_livro

livro_bp = Blueprint('livro_bp', __name__)

@livro_bp.route('/livro', methods=['POST'])
def create_livro_route():
    data = request.json
    create_livro(data)
    return jsonify({"message": "Livro inserted successfully"}), 201

@livro_bp.route('/livro', methods=['GET'])
def get_livros_route():
    livros = get_livros()
    return jsonify(livros), 200

@livro_bp.route('/livro/<int:id>', methods=['PUT'])
def update_livro_route(id):
    data = request.json
    update_livro(id, data)
    return jsonify({"message": "Livro updated successfully"}), 200

@livro_bp.route('/livro/<int:id>', methods=['DELETE'])
def delete_livro_route(id):
    delete_livro(id)
    return jsonify({"message": "Livro deleted successfully"}), 200
