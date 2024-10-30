from flask import Blueprint, request, jsonify
from model.emprestimo_model import create_emprestimo, find_usuario_by_nome_email

emprestimo_bp = Blueprint('emprestimo_bp', __name__)

# Rota para criar empréstimo
@emprestimo_bp.route("/emprestimo", methods=['POST'])
def create_emprestimo_route():
    data = request.json
    
    # Verificação dos dados necessários
    if not data or not 'usuario' or not 'livro' in data or not ('data_emprestimo' in data and 'data_devolucao' in data):
        return jsonify({
            "message": "Dados insuficientes para criar o empréstimo. Informe 'nome' ou 'email', 'titulo' ou 'idlivro', 'data_emprestimo' e 'data_devolucao'."
        }), 400

    # Buscar o usuário com base em nome ou email
    usuario = find_usuario_by_nome_email(nome=data.get('nome'), email=data.get('email'))
    if not usuario:
        return jsonify({"message": "Usuário não encontrado."}), 404

    # Chama a função de criação do empréstimo usando o ID do usuário encontrado
    try:
        resultado = create_emprestimo(
            usuario_id=usuario['id'],
            livro=data.get('livro'),
            data_emprestimo=data.get('data_emprestimo'),
            data_devolucao=data.get('data_devolucao')
        )
        
        if resultado:
            return jsonify({"message": resultado}), 201
        else:
            return jsonify({"message": "Erro ao criar o empréstimo."}), 500
    except Exception as e:
        return jsonify({"message": f"Erro interno ao criar o empréstimo: {str(e)}"}), 500




        