from mysql.connector import Error
from .Server import create_server_connection, execute_query, read_query

# Criação de usuário
def create_usuario(data):
    query = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
    conexao = None
    
    try:
        conexao = create_server_connection()
        if conexao:
            execute_query(conexao, query, (data['nome'], data['email'],data['senha']))

    except Error as e:
        print(f"Erro ao criar o usuário: {e}")
        return {"message": f"Erro ao criar o usuário: {str(e)}"}, 500
        
    finally:
        # Garante que a conexão será fechada
        if conexao:
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

        if resultado:  
            usuario = resultado[0] 
            if check_password_hash(usuario[3],senha):  
                return usuario 
            else:
                print("Senha incorreta")
                return None  
        else:
            print("Email incorreta")
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
