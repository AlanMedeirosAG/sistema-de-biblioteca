from mysql.connector import Error
from werkzeug.security import check_password_hash
from .Server import create_server_connection, execute_query, read_query

# Criação de usuário
def create_usuario(data):
    query = "INSERT INTO usuario (nome, email, senha, tipo_usuario) VALUES (%s, %s, %s, %s)"
    conexao = create_server_connection()
    
    try:
        if conexao:
            execute_query(conexao, query, (data['nome'], data['email'],(data['senha']), data['tipo_usuario']))
    except Exception as e:
        print(f"Erro ao inserir usuário: {str(e)}")
    finally:
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

def pesquisaUsuario(email=None, nome=None):
    query = "SELECT * FROM usuario WHERE "
    
    # Verifica se foi passado o email ou o nome
    if email:
        query += "email = %s"
        valores = (email,)
    elif nome:
        query += "nome LIKE %s"
        valores = ('%' + nome + '%',)  # Faz uma busca parcial no nome
    else:
        print("Erro: É necessário informar um e-mail ou nome para a pesquisa.")
        return None

# Buscar login de usuário
def get_usuario_login(email, senha):
    query = "SELECT * FROM usuario WHERE email = %s"
    conexao = create_server_connection()
    
    if conexao:
        resultado = read_query(conexao, query, (email,))
        conexao.close()

        if resultado:  
            usuario = resultado[0] 
            if check_password_hash(usuario[3], senha):  
                return {
                    "id": usuario[0],
                    "nome": usuario[1]   ,      
                    "email": usuario[2],       
                    "tipo": usuario[4]         
                }
            else:
                print("Senha incorreta")
                return None  
        else:
            print("E-mail incorreto")
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
