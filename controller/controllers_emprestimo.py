from flask import Blueprint, request, jsonify
from datetime import datetime
from model.emprestimo_model import create_emprestimo, find_usuario_by_nome_email,verifica_livro_bd,create_devolucao,find_historico_by_id

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
    titulo = livro_info if isinstance(data.get('livro'), str) else None
    idlivro = livro_info if isinstance(data.get('livro'), int) else None

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


@emprestimo_bp.route("/emprestimo", methods=['PUT'])
def book_return_route():
    data = request.json
    
    print(data)

    # Verificação dos dados necessários
    if not data or 'idhistorico' not in data or 'livro' not in data:
        return jsonify({"message": "Dados insuficientes para processar a devolução."}), 400

    livro_info = data.get('livro')
    livro_id = None
    livro_titulo = None

    if isinstance(livro_info, dict):  # Quando livro é um dicionário
        livro_id = livro_info.get('idlivro')
        livro_titulo = livro_info.get('livro')
    elif isinstance(livro_info, int):  # Quando livro é um ID (inteiro)
        livro_id = livro_info
    elif isinstance(livro_info, str):  # Quando livro é um título (string)
        livro_titulo = livro_info

    try:
        # Busca informações do histórico pelo idhistorico
        historico = find_historico_by_id(data['idhistorico'])
        if not historico:
            return jsonify({"message": "Histórico não encontrado."}), 404

        # Verifica se já foi devolvido
        if historico.get('devolvido', False):  # Verificando se já foi devolvido
            return jsonify({"message": "Este empréstimo já foi devolvido."}), 400

        # Adicionar validação para o livro (opcional)
        if livro_id is None and livro_titulo is None:
            return jsonify({"message": "Dados do livro inválidos."}), 400

        # Atualiza o histórico para marcar como devolvido
        resultado = create_devolucao(
            idhistorico=data['idhistorico'],
            livro_id=livro_id,
            livro_titulo=livro_titulo,
        )

        if resultado:
            return jsonify({"message": resultado}), 200
        else:
            return jsonify({"message": "Erro ao registrar a devolução."}), 500

    except Exception as e:
        import traceback
        print("Erro interno:", traceback.format_exc())
        return jsonify({"message": f"Erro interno na devolução: {str(e)}"}), 500
        
