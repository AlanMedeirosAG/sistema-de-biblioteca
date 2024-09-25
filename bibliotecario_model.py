from mysql.connector import Error
from .Server import create_server_connection, execute_query, read_query

def create_bibliotecario(data):
    query = "INSERT INTO bibliotecario (nome, email, senha) VALUES (%s, %s, %s)"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['nome'], data['email'], data['senha']))
        conexao.close()
       

def get_bibliotecarios():
    query = "SELECT * FROM bibliotecario"
    conexao = create_server_connection()
    if conexao:
        resultado = read_query(conexao, query)
        conexao.close()

def update_bibliotecario(id,data):
    query = "UPDATE bibliotecario SET nome = %s, email = %s, senha = %s WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['nome'], data['email'], data['senha'], id))
        conexao.close()


def delete_bibliotecario(id):
    query = "DELETE FROM bibliotecario WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (id,))
        conexao.close()