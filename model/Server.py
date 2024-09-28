import mysql.connector
from mysql.connector import Error

def create_server_connection():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='16012023MA',
            database='bdgerencia',
        )
        return conexao
    except Error as err:
        print(f"Error: '{err}'")
        return None

def execute_query(conexao, query, data=None):
    cursor = conexao.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        conexao.commit()
        return cursor
    except Error as err:
        print(f"Error: '{err}'")
        return None
    finally:
        cursor.close()

def read_query(conexao, query, data=None):
    cursor = conexao.cursor()
    resultado = None
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        resultado = cursor.fetchall()
        return resultado
    except Error as err:
        print(f"Error: '{err}'")
        return None
    finally:
        cursor.close()
