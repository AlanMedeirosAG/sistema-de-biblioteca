from mysql.connector import Error
from .Server import create_server_connection, execute_query, read_query

def create_administrador(data):
    query = "INSERT INTO administrador (nome, email, senha) VALUES (%s, %s, %s)"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['nome'], data['email'], data['senha']))
        conexao.close()
       

def get_administradores():
    query = "SELECT * FROM administrador"
    conexao = create_server_connection()
    if conexao:
        resultado = read_query(conexao, query)
        conexao.close()

def update_administrador(id,data):
    query = "UPDATE administrador SET nome = %s, email = %s, senha = %s WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['nome'], data['email'], data['senha'], id))
        conexao.close()


def delete_administrador(id):
    query = "DELETE FROM administrador WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (id,))
        conexao.close()