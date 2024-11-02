from mysql.connector import Error
from werkzeug.security import check_password_hash
from .Server import create_server_connection, execute_query, read_query

def create_emprestimo(idusuario, livro_id=None, livro_titulo=None, data_emprestimo=None, data_devolucao=None):
    # Query para inserir o empréstimo com datas fornecidas
    query_emprestimo = """
        INSERT INTO historico (idusuario, livro, multa, data_emprestimo, data_devolucao)
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
            
            if livro and livro[0] > 0:
                # Inserir o empréstimo com as datas
                cursor.execute(query_emprestimo, (idusuario, livro_id or livro_titulo, data_emprestimo, data_devolucao))
                
                # Atualizar a quantidade do livro
                cursor.execute("UPDATE livro SET quantidade = quantidade - 1 WHERE idlivro = %s OR titulo = %s",(livro_id, livro_titulo))

                
                # Commit para salvar as alterações
                conexao.commit()
                
                return f"Empréstimo realizado com sucesso! Livro ID: {livro_id} para o usuário ID: {idusuario}"
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
    
def create_devolucao(idhistorico,livro_id = None,livro_titulo = None):
  
    # Criar a conexao
    conexao = create_server_connection()
  
    if conexao:
        try:
            cursor = conexao.cursor()
            
            # Atualiza a data de devolução no histórico
            cursor.execute("""
                UPDATE historico
                SET data_devolucao = NOW()  -- Define a data de devolução como a data atual
                WHERE idhistorico = %s
            """, (idhistorico,))
          
            # Atualiza a quantidade de livros na tabela
            if livro_id:
                cursor.execute("UPDATE livro SET quantidade = quantidade + 1 WHERE idlivro = %s", (livro_id,))
            elif livro_titulo:
                cursor.execute("UPDATE livro SET quantidade = quantidade + 1 WHERE titulo = %s", (livro_titulo,))
        
            conexao.commit()
        
            return f"Devolução registrada com sucesso! ID do emprestimo:{idhistorico}"
    
        except Exception as e:
            conexao.rollback() # Reverte em caso de erro
            print(f"Erro ao registrar devolução: {e}")
            
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Erro na conexao com o banco de dados.")
        return None
    

# Função para buscar usuário pelo nome ou email
def find_usuario_by_nome_email(nome=None, email=None):
    query = """
        SELECT idusuario, nome, email
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
    
# Função para buscar livro pelo titulo ou id
def verifica_livro_bd(titulo=None, idlivro=None):
    query = """
        SELECT idlivro, titulo
        FROM livro
        WHERE (titulo = %s OR idlivro = %s)
        LIMIT 1
    """
    
    conexao = create_server_connection()
    if conexao:
        try:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(query, (titulo, idlivro))
            livro = cursor.fetchone()  # Busca um único livro que corresponde ao critério
            return livro is not None  # Retorna o dicionário do livro ou None se não encontrado
        except Exception as e:
            print(f"Erro ao verificar livro: {e}")
            return None
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Erro na conexão com o banco de dados.")
        return None
