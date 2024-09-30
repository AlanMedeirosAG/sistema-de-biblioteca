from mysql.connector import Error
from .Server import create_server_connection, execute_query, read_query

def create_historico(data):
    query = "INSERT INTO historico (usuario_id, livro_id, data_emprestimo, data_devolucao) VALUES (%s, %s, %s, %s)"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (
            data['usuario_id'], data['livro_id'], data['data_emprestimo'], data.get('data_devolucao')
        ))
        conexao.close()

def get_historico():
    query = "SELECT * FROM historico"
    conexao = create_server_connection()
    if conexao:
        resultado = read_query(conexao, query)
        conexao.close()
        return resultado

def update_historico(id,data):
    query = "UPDATE historico SET usuario_id = %s, livro_id = %s, data_emprestimo = %s, data_devolucao = %s WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (
            data['usuario_id'], data['livro_id'], data['data_emprestimo'], data['data_devolucao'], id
        ))
        conexao.close()
        
def delete_historico(id):
    query = "DELETE FROM historico WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (id,))
        conexao.close()
