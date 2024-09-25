from mysql.connector import Error
from .Server import create_server_connection, execute_query, read_query

def create_estoque(data):
    query = "INSERT INTO estoque (livro_id, quantidade) VALUES (%s, %s)"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['livro_id'], data['quantidade']))
        conexao.close()

def get_estoque():
    query = "SELECT * FROM estoque"
    conexao = create_server_connection()
    if conexao:
        resultado = read_query(conexao, query)
        conexao.close()

def update_estoque(id,data):
    query = "UPDATE estoque SET livro_id = %s, quantidade = %s WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['livro_id'], data['quantidade'], id))
        conexao.close()

def delete_estoque(id):
    query = "DELETE FROM estoque WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (id,))
        conexao.close()