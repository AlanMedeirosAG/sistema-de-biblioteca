from mysql.connector import Error
from .Server import create_server_connection, execute_query, read_query

# Criação de usuário
def create_usuario(data):
    query = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['nome'], data['email'], data['senha']))
        conexao.close()

# Retornar todos os usuários
def get_usuarios():
    query = "SELECT * FROM usuario"
    conexao = create_server_connection()
    if conexao:
        resultado = read_query(conexao, query)
        conexao.close()
        return resultado

# Buscar login de usuário
def get_usuario_login(email, senha):
    query = "SELECT * FROM usuario WHERE email = %s"
    conexao = create_server_connection()
    if conexao:
        resultado = read_query(conexao, query, (email,))
        conexao.close()

        # Verificação de senha
        if resultado and resultado[0]['senha'] == senha:
            return resultado[0]
        else:
            return None

# Atualizar usuário
def update_usuario(id, data):
    query = "UPDATE usuario SET nome = %s, email = %s, senha = %s WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['nome'], data['email'], data['senha'], id))
        conexao.close()

# Deletar usuário
def delete_usuario(id):
    query = "DELETE FROM usuario WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (id,))
        conexao.close()
