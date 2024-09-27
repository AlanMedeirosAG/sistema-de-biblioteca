from mysql.connector import Error
from .Server import create_server_connection, execute_query, read_query

def create_livro(data):
    query = "INSERT INTO livro (titulo, autor, ano_publicacao, isbn) VALUES (%s, %s, %s, %s)"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['titulo'], data['autor'], data.get('ano_publicacao'), data.get('isbn')))
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
