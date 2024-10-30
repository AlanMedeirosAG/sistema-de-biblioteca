from mysql.connector import Error
from werkzeug.security import check_password_hash
from .Server import create_server_connection, execute_query, read_query

def create_emprestimo(usuario_id, livro_id=None, livro_titulo=None, data_emprestimo=None, data_devolucao=None):
    # Query para inserir o empréstimo com datas fornecidas
    query_emprestimo = """
        INSERT INTO historico (usuario_id, livro, multa, Now(), data_devolucao)
        VALUES (%s, %s, NULL, %s, %s)
    """
    #Emprestimo de uma semana com o Now()
    
    # Criar conexão com o banco de dados
    conexao = create_server_connection()
    
    if conexao:
        try:
            cursor = conexao.cursor()
            
            # Verificar se o livro está disponível
            if livro_id:
                cursor.execute("SELECT quantidade FROM livro WHERE idlivro = %s", (livro_id,))
            elif livro_titulo:
                cursor.execute("SELECT quantidade FROM livro WHERE titulo = %s", (livro_titulo,))    
                
            livro = cursor.fetchone()
            
            if livro and livro['quantidade'] > 0:
                # Inserir o empréstimo com as datas
                cursor.execute(query_emprestimo, (usuario_id, livro_id or livro_titulo, data_emprestimo, data_devolucao))
                
                # Atualizar a quantidade do livro
                cursor.execute("UPDATE livro SET quantidade = quantidade - 1 WHERE idlivro = %s OR titulo = %s",(livro_id, livro_titulo))

                
                # Commit para salvar as alterações
                conexao.commit()
                
                return f"Empréstimo realizado com sucesso! Livro ID: {livro_id} para o usuário ID: {usuario_id}"
            else:
                return "Livro não disponível para empréstimo."
        
        except Exception as e:
            conexao.rollback()  # Reverte em caso de erro
            print(f"Erro ao registrar empréstimo: {e}")
            return None
        
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Erro na conexão com o banco de dados.")
        return None

# Função para buscar usuário pelo nome ou email
def find_usuario_by_nome_email(nome=None, email=None):
    query = """
        SELECT id, nome, email
        FROM usuario
        WHERE (nome = %s OR email = %s)
        LIMIT 1
    """
    
    conexao = create_server_connection()
    if conexao:
        try:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(query, (nome, email))
            usuario = cursor.fetchone()  # Busca um único usuário que corresponde ao critério
            return usuario  # Retorna o dicionário do usuário ou None se não encontrado
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return None
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Erro na conexão com o banco de dados.")
        return None