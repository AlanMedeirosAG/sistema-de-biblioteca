from mysql.connector import Error
from werkzeug.security import check_password_hash
from .Server import create_server_connection, execute_query, read_query

#Função que cria um novo bibliotecario atraves de uma query
def create_bibliotecario(data):
    # Inserir o novo usuário na tabela 'usuario'
    query_usuario = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
    conexao = create_server_connection()
    
    try:
        if conexao:
            # Inserir o usuário
            execute_query(conexao, query_usuario, (data['nome'], data['email'],(data['senha'])))
            
            # Obter o id do usuário recém-inserido
            query_id = "SELECT LAST_INSERT_ID()"
            cursor = conexao.cursor()
            cursor.execute(query_id)
            idusuario = cursor.fetchone()[0]  # Pega o primeiro valor da tupla retornada
            
            # Inserir o bibliotecário na tabela 'bibliotecario'
            query_bibliotecario = "INSERT INTO bibliotecario (idusuario) VALUES (%s)"
            execute_query(conexao, query_bibliotecario, (idusuario,))
            
    except Exception as e:
        print(f"Erro ao inserir bibliotecário: {str(e)}")
    
    finally:
        if conexao:
            conexao.close()
       
#Função que obtem os bibliotecarios atraves de uma query
def get_bibliotecarios():
    query = "SELECT * FROM bibliotecario"
    conexao = create_server_connection()
    if conexao:
        resultado = read_query(conexao, query)
        conexao.close()

#Função que faz login de um bibliotecario atraves de uma query
def get_bibliotecario_login(email, senha):
    query = """
    SELECT u.id, u.email, u.senha  -- Pegamos apenas o necessário (id, email, senha)
    FROM usuario u
    INNER JOIN bibliotecario b ON u.id = b.idusuario
    WHERE u.email = %s
    """
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

#Função que atualiza um bibliotecario atraves de uma query
def update_bibliotecario(id,data):
    query = "UPDATE bibliotecario SET nome = %s, email = %s, senha = %s WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['nome'], data['email'], data['senha'], id))
        conexao.close()

#Função que atualiza um bibliotecario atraves de uma query
def delete_bibliotecario(id):
    query = "DELETE FROM bibliotecario WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (id,))
        conexao.close()