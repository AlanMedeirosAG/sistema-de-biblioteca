from mysql.connector import Error
from werkzeug.security import check_password_hash
from .Server import create_server_connection, execute_query, read_query
from datetime import datetime

def create_emprestimo(idusuario, livro_id=None, livro_titulo=None, data_emprestimo=None, data_devolucao=None):
    if not livro_id and not livro_titulo:
        return "É necessário fornecer o ID ou o título do livro."

    # Query para inserir o empréstimo com datas fornecidas
    query_emprestimo = """
        INSERT INTO historico (idusuario, livro, multa, data_emprestimo, data_devolucao)
        VALUES (%s, %s, NULL, %s, %s)
    """
        
    conexao = create_server_connection()
    
    if conexao:
        try:
            cursor = conexao.cursor()
            
            # Verificar disponibilidade do livro
            cursor.execute("""
                SELECT quantidade 
                FROM livro 
                WHERE idlivro = %s OR titulo = %s
            """, (livro_id, livro_titulo))
                
            livro = cursor.fetchone()
            
            if not livro:
                return "Livro não encontrado."
            if livro[0] > 0:
                # Inserir o empréstimo
                cursor.execute(query_emprestimo, (idusuario, livro_id or livro_titulo, data_emprestimo, data_devolucao))
                
                # Atualizar a quantidade do livro
                cursor.execute("""
                    UPDATE livro 
                    SET quantidade = quantidade - 1 
                    WHERE idlivro = %s OR titulo = %s
                """, (livro_id, livro_titulo))
                
                conexao.commit()
                return f"Empréstimo realizado com sucesso! Livro ID: {livro_id or livro_titulo} para o usuário ID: {idusuario}"
            else:
                return "Livro não disponível para empréstimo."
        
        except Exception as e:
            conexao.rollback()
            print(f"Erro ao registrar empréstimo: {e}")
            return None
        
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Erro na conexão com o banco de dados.")
        return None
    
def create_devolucao(idhistorico, livro_id=None, livro_titulo=None, multa=0):
    if not idhistorico:
        return "É necessário fornecer o ID do histórico."

    conexao = create_server_connection()
  
    if conexao:
        try:
            cursor = conexao.cursor()
            
            # Verificar se o histórico já foi devolvido
            cursor.execute(""" 
                SELECT devolvido 
                FROM historico 
                WHERE idhistorico = %s
            """, (idhistorico,))
            historico = cursor.fetchone()
            
            if not historico:
                return "Histórico não encontrado."
            
            if historico[0]:  # Caso tenha 1 na coluna "devolvido"
                return "Este empréstimo já foi devolvido."
            
            # Atualizar histórico com a devolução
            cursor.execute("""
                UPDATE historico
                SET data_devolucao = NOW(), multa = %s, devolvido = 1
                WHERE idhistorico = %s
            """, (multa, idhistorico))
          
            # Atualizar quantidade do livro
            if livro_id:
                cursor.execute("UPDATE livro SET quantidade = quantidade + 1 WHERE idlivro = %s", (livro_id,))
            elif livro_titulo:
                cursor.execute("UPDATE livro SET quantidade = quantidade + 1 WHERE titulo = %s", (livro_titulo,))
            else:
                raise ValueError("Nem ID nem título do livro foram fornecidos.")
            
            conexao.commit()
        
            return f"Devolução registrada com sucesso! ID do empréstimo: {idhistorico}, Multa: R${multa:.2f}"
    
        except Exception as e:
            conexao.rollback()
            print(f"Erro ao registrar devolução: {e}")
            return None
        
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Erro na conexão com o banco de dados.")
        return None


# Função para buscar usuário pelo nome ou email
def find_usuario_by_nome_email(nome=None, email=None):
    if not nome and not email:
        print("Nome ou email devem ser fornecidos para buscar o usuário.")
        return None

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
            if not usuario:
                return None  # ou uma mensagem clara sobre não encontrado
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
    if not titulo and not idlivro:
        print("Título ou ID do livro devem ser fornecidos para verificar o livro.")
        return None

    query = """
        SELECT idlivro, titulo, quantidade
        FROM livro
        WHERE (titulo = %s OR idlivro = %s)
        LIMIT 1
    """
    
    conexao = create_server_connection()
    if conexao:
        try:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(query, (titulo, idlivro))
            livro = cursor.fetchone()
            if not livro:
                return None  # ou uma mensagem clara sobre não encontrado
            return livro  # Retorna o dicionário do livro ou None
        except Exception as e:
            print(f"Erro ao verificar livro: {e}")
            return None
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Erro na conexão com o banco de dados.")
        return None

def find_historico_by_id(idhistorico):
    if not idhistorico:
        print("ID do histórico deve ser fornecido para buscar o histórico.")
        return None

    query = """
        SELECT idhistorico, livro, multa, data_emprestimo, data_devolucao, idusuario, devolvido
        FROM historico
        WHERE idhistorico = %s
        LIMIT 1
    """

    conexao = create_server_connection()
    if conexao:
        try:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(query, (idhistorico,))
            historico = cursor.fetchone()
            return historico
        except Exception as e:
            print(f"Erro ao buscar histórico: {e}")
            return None
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Erro na conexão com o banco de dados.")
        return None

def find_emprestimos_nao_devolvidos(idusuario):
    query = """
        SELECT idhistorico, livro, data_emprestimo, data_devolucao 
        FROM historico
        WHERE idusuario = %s AND devolvido = 0
    """
    conexao = create_server_connection()
    if conexao:
        try:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(query, (idusuario,))
            emprestimos = cursor.fetchall()
            return emprestimos
        except Exception as e:
            print(f"Erro ao buscar empréstimos não devolvidos: {e}")
            return None
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Erro na conexão com o banco de dados.")
        return None

# Função para visualizar a multa antes de devolver
def visualizar_multa(idhistorico, livro_id=None, livro_titulo=None, multa_por_dia=2.00):
    if not idhistorico:
        return "É necessário fornecer o ID do histórico."

    conexao = create_server_connection()
  
    if conexao:
        try:
            cursor = conexao.cursor()

            # Buscar o histórico do empréstimo
            cursor.execute("""
                SELECT devolvido, data_emprestimo 
                FROM historico 
                WHERE idhistorico = %s
            """, (idhistorico,))
            historico = cursor.fetchone()
            
            if not historico:
                return "Histórico não encontrado."
            
            if historico[0]:  # Se o livro já foi devolvido
                return "Este empréstimo já foi devolvido."
            
            data_emprestimo = historico[1]  # Data do empréstimo
            data_atual = datetime.now()  # Data atual (data de devolução)

            # Calcular a diferença de dias entre a data de devolução e a data de empréstimo
            dias_atraso = (data_atual - data_emprestimo).days
            
            # Se o livro for devolvido antes da data de empréstimo, não há multa
            multa = 0
            if dias_atraso > 0:
                multa = dias_atraso * multa_por_dia  # Multa por atraso

            return f"A multa estimada para a devolução é de R${multa:.2f}."
    
        except Exception as e:
            print(f"Erro ao calcular multa: {e}")
            return None
        
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Erro na conexão com o banco de dados.")
        return None
