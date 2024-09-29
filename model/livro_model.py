from mysql.connector import Error
from .Server import create_server_connection, execute_query, read_query

def create_livro(data):
    # Query para inserir o livro
    query_livro = "INSERT INTO livro (titulo, autor, ano_lancamento, isbn, genero) VALUES (%s, %s, %s, %s, %s)"
    conexao = create_server_connection()
    
    if conexao:
        try:
            # Inserir o livro e obter o ID gerado
            cursor = conexao.cursor()
            cursor.execute(query_livro, (
                data['titulo'], 
                data['autor'], 
                data.get('ano_lancamento'), 
                str(data.get('isbn')), 
                data['genero']
            ))
            idlivro = cursor.lastrowid  # Obtém o ID do livro inserido
            
            # Query para inserir no estoque
            query_estoque = "INSERT INTO estoque (idlivro, numero_de_livros) VALUES (%s, %s)"
            numero_de_livros = data.get('quantidade', 1)  # Padrão de 1 se não for fornecida
            
            # Inserir no estoque com o ID do livro
            cursor.execute(query_estoque, (idlivro, numero_de_livros))
            
            # Commit para salvar as alterações
            conexao.commit()
            
            # Retornar o ID do livro inserido
            return idlivro
        
        except Exception as e:
            conexao.rollback()  # Reverte em caso de erro
            print(f"Erro ao inserir livro e estoque: {e}")
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
