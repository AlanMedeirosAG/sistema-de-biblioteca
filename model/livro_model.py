from mysql.connector import Error
from .Server import create_server_connection, execute_query, read_query

#Função que cria livro atraves de uma query
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

#Função que obtem todos os livros atraves de uma query
def get_livros():
    query = "SELECT * FROM livro"
    conexao = create_server_connection()
    if conexao:
        resultado = read_query(conexao, query)
        conexao.close()
        print(resultado)
        return resultado

#Função que busca um livro atraves de uma query
def pesquisaLivro(titulo=None, idlivro=None):
    query = "SELECT * FROM livro WHERE "
    
    # Verifica se foi passado o idlivro ou o nome
    if idlivro:
        query += "idlivro = %s"
        valores = (idlivro,)
    elif titulo:
        query += "titulo LIKE %s"
        valores = ('%' + titulo + '%',)  # Faz uma busca parcial no nome
    else:
        print("Erro: É necessário informar um ID ou nome para a pesquisa.")
        return None
    
    cursor = conexao.cursor()
    cursor.execute(query, valores)
    resultado = cursor.fetchall()

    # Transforma o resultado em uma lista de dicionários
    livros = []
    for livro in resultado:
        livro_dict = {
            "idlivro": livro[0],
            "titulo": livro[1],
            "autor": livro[2],
            "isbn": livro[3],
            "genero": livro[4],
            "campo_adicional": livro[5],  # Altere para o nome correto da coluna se necessário
            "quantidade": livro[6]
        }
        livros.append(livro_dict)

        return livros if livros else None  # Retorna a lista ou None se vazia
    
    # Cria conexão com o banco de dados
    conexao = create_server_connection()
    
    if conexao:
        try:
            # Executa a consulta com os valores fornecidos
            resultado = read_query(conexao, query, valores)
            conexao.close()
            print(resultado)
            return resultado
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")
            conexao.close()
            return None
    else:
        print("Erro ao conectar com o banco de dados.")
        return None

#Função que atualiza um livro atraves de uma query
def update_livro(id, data):
    query = "UPDATE livro SET titulo = %s, autor = %s, ano_publicacao = %s, isbn = %s WHERE idlivro = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['titulo'], data['autor'], data.get('ano_publicacao'), data.get('isbn'), id))
        conexao.close()

#Função que deleta um livro atraves de uma query
def delete_livro(id):
    query = "DELETE FROM livro WHERE idlivro = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (id,))
        conexao.close()
