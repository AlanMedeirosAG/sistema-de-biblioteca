from mysql.connector import Error
from .Server import create_server_connection, execute_query, read_query

def create_livro(data):
    # Query para inserir o livro
    query_livro = "INSERT INTO livro (titulo, autor, ano_lancamento, isbn, genero, quantidade) VALUES (%s, %s, %s, %s, %s, %s)"
    conexao = create_server_connection()
    
    if conexao:
        try:
            # Inserir o livro e obter o ID gerado
            cursor = conexao.cursor()
            cursor.execute(query_livro,(
                data['titulo'], 
                data['autor'], 
                data.get('ano_lancamento'), 
                str(data.get('isbn')), 
                data['genero'],
                data['quantidade']
            ))
            idlivro = cursor.lastrowid  # Obtém o ID do livro inserido
            
            # Commit para salvar as alterações
            conexao.commit()
            
            # Retornar o ID do livro inserido
            return idlivro
        
        except Exception as e:
            conexao.rollback()  # Reverte em caso de erro
            print(f"Erro ao inserir livro: {e}")
            return None
        
        finally:
            # Fechar conexão
            cursor.close()
            conexao.close()

def get_livros():
    query = "SELECT * FROM livro"
    conexao = create_server_connection()
    if conexao:
        resultado = read_query(conexao, query)
        conexao.close()
        return resultado

def update_livro(id, data):
    query = "UPDATE livro SET titulo = %s, autor = %s, ano_publicacao = %s, isbn = %s WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['titulo'], data['autor'], data.get('ano_publicacao'), data.get('isbn'), id))
        conexao.close()

def delete_livro(id):
    query = "DELETE FROM livro WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (id,))
        conexao.close()
