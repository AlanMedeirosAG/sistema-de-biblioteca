from mysql.connector import Error
from datetime import datetime,date
from .Server import create_server_connection, execute_query, read_query

#Função que cria o historico atraves de uma query
def create_historico(data):
    query = "INSERT INTO historico (usuario_id, livro_id, data_emprestimo, data_devolucao) VALUES (%s, %s, %s, %s)"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (
            data['usuario_id'], data['livro_id'], data['data_emprestimo'], data.get('data_devolucao')
        ))
        conexao.close()

#Função que obtem todos os historicos atraves de uma query
def get_historico():
    query = "SELECT idhistorico, livro, multa, data_emprestimo, data_devolucao,idusuario, devolvido FROM historico"
    conexao = create_server_connection()
    if conexao:
        resultado = read_query(conexao, query)
        conexao.close()

        print(resultado)
        
        # Calculando a multa para cada histórico
        historicos_com_multa = []
        for historico in resultado:
            idhistorico = historico[0]
            livro = historico[1]
            data_emprestimo = historico[3]
            data_devolucao = historico[4]
            idusuario = historico[5]
            devolvido = historico[6]
            
            # Calcula a multa
            multa = calcular_multa(data_devolucao)

            # Adiciona a multa ao dicionário de histórico
            historicos_backend = {
                "idhistorico": idhistorico,
                "livro": livro,
                "multa": multa,
                "data_emprestimo": data_emprestimo,
                "data_devolucao": data_devolucao,
                "idusuario": idusuario,
                "devolvido": devolvido
            }
            historicos_com_multa.append(historicos_backend)

        return historicos_com_multa


#Função que atualiza o historico atraves de uma query
def update_historico(id,data):
    query = "UPDATE historico SET usuario_id = %s, livro_id = %s, data_emprestimo = %s, data_devolucao = %s WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (
            data['usuario_id'], data['livro_id'], data['data_emprestimo'], data['data_devolucao'], id
        ))
        conexao.close()

#Função que deleta o historico atraves de uma query
def delete_historico(id):
    query = "DELETE FROM historico WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (id,))
        conexao.close()
 
# Função que calcula a media de acordo com um valor diario multiplicnado pela diferença de atraso e devolução       
def calcular_multa(data_devolucao, valor_diario=0.5):
    
    # Se data_devolucao for uma string, converte para datetime
    if isinstance(data_devolucao, str):
        formato_data = "%Y-%m-%d"
        data_devolucao = datetime.strptime(data_devolucao, formato_data)

    data_atual = datetime.now()

    if isinstance(data_devolucao, datetime):
        pass  # Já é datetime
    elif isinstance(data_devolucao, date):
        data_devolucao = datetime.combine(data_devolucao, datetime.min.time())

    # Calcula o atraso (em dias)
    atraso = (data_atual - data_devolucao).days

    # Se o livro foi devolvido após a data de devolução, calcula a multa
    if atraso > 0:
        multa = atraso * valor_diario
    else:
        multa = 0.0

    return multa
