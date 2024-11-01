from flask import Blueprint, request, jsonify
from model.emprestimo_model import create_emprestimo, find_usuario_by_nome_email,verifica_livro_bd

emprestimo_bp = Blueprint('emprestimo_bp', __name__)

# Rota para criar empréstimo
@emprestimo_bp.route("/emprestimo", methods=['POST'])
def create_emprestimo_route():
    data = request.json
    
    # Verificação dos dados necessários
    if not data or 'usuario' not in data or 'livro' not in data or 'data_emprestimo' not in data or 'data_devolucao' not in data:
        return jsonify({
            "message": "Dados insuficientes para criar o empréstimo. Informe 'nome' ou 'email', 'titulo' ou 'idlivro', 'data_emprestimo' e 'data_devolucao'."
        }), 400

    #Extrair o nome ou email do usuário
    usuario_info = data.get('usuario')
    nome = usuario_info if '@' not in usuario_info else None
    email = usuario_info if '@' in usuario_info else None


    # Buscar o usuário com base em nome ou email
    usuario = find_usuario_by_nome_email(nome=nome, email=email)
    if not usuario:
        return jsonify({"message": "Usuário não encontrado."}), 404
    
    livro_info = data.get('livro')
    titulo = livro_info if isinstance(data.get('livro'), int) else None
    idlivro = livro_info if isinstance(data.get('livro'), str) else None

    livro = verifica_livro_bd(titulo=titulo,idlivro=idlivro)
    if not livro:
        return jsonify({"message": "Livro não encontrado."}), 404
            

    # Chama a função de criação do empréstimo usando o ID do usuário encontrado
    try:
        resultado = create_emprestimo(
            idusuario=usuario['idusuario'],
            livro_id=data.get('livro') if isinstance(data.get('livro'), int) else None,  # Se for um ID numérico
            livro_titulo=data.get('livro') if isinstance(data.get('livro'), str) else None,  # Se for o título do livro 
            data_emprestimo=data.get('data_emprestimo'),
            data_devolucao=data.get('data_devolucao')
        )
        
        if resultado:
            return jsonify({"message": resultado}), 201
        else:
            return jsonify({"message": "Erro ao criar o empréstimo."}), 500
    except Exception as e:
        import traceback
        print("Erro interno:", traceback.format_exc())
        return jsonify({"message": f"Erro interno ao criar o empréstimo: {str(e)}"}), 500
        
