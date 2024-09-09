from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

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

# CRUD for livro
@app.route('/livro', methods=['POST'])
def create_livro():
    data = request.json
    query = "INSERT INTO livro (titulo, autor, ano_publicacao, isbn) VALUES (%s, %s, %s, %s)"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['titulo'], data['autor'], data.get('ano_publicacao'), data.get('isbn')))
        conexao.close()
        return jsonify({"message": "Livro inserted successfully"}), 201
    else:
        return jsonify({"message": "Database connection failed"}), 500

@app.route('/livro', methods=['GET'])
def get_livros():
    query = "SELECT * FROM livro"
    conexao = create_server_connection()
    if conexao:
        resultado = read_query(conexao, query)
        conexao.close()
        return jsonify(resultado), 200
    else:
        return jsonify({"message": "Database connection failed"}), 500

@app.route('/livro/<int:id>', methods=['PUT'])
def update_livro(id):
    data = request.json
    query = "UPDATE livro SET titulo = %s, autor = %s, ano_publicacao = %s, isbn = %s WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['titulo'], data['autor'], data.get('ano_publicacao'), data.get('isbn'), id))
        conexao.close()
        return jsonify({"message": "Livro updated successfully"}), 200
    else:
        return jsonify({"message": "Database connection failed"}), 500

@app.route('/livro/<int:id>', methods=['DELETE'])
def delete_livro(id):
    query = "DELETE FROM livro WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (id,))
        conexao.close()
        return jsonify({"message": "Livro deleted successfully"}), 200
    else:
        return jsonify({"message": "Database connection failed"}), 500

# Similar CRUD operations for usuario, bibliotecario, administrador, estoque, and historico

# CRUD for usuario
@app.route('/usuario', methods=['POST'])
def create_usuario():
    data = request.json
    query = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['nome'], data['email'], data['senha']))
        conexao.close()
        return jsonify({"message": "Usuario inserted successfully"}), 201
    else:
        return jsonify({"message": "Database connection failed"}), 500

@app.route('/usuario', methods=['GET'])
def get_usuarios():
    query = "SELECT * FROM usuario"
    conexao = create_server_connection()
    if conexao:
        resultado = read_query(conexao, query)
        conexao.close()
        return jsonify(resultado), 200
    else:
        return jsonify({"message": "Database connection failed"}), 500

@app.route('/usuario/<int:id>', methods=['PUT'])
def update_usuario(id):
    data = request.json
    query = "UPDATE usuario SET nome = %s, email = %s, senha = %s WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (data['nome'], data['email'], data['senha'], id))
        conexao.close()
        return jsonify({"message": "Usuario updated successfully"}), 200
    else:
        return jsonify({"message": "Database connection failed"}), 500

@app.route('/usuario/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    query = "DELETE FROM usuario WHERE id = %s"
    conexao = create_server_connection()
    if conexao:
        execute_query(conexao, query, (id,))
        conexao.close()
        return jsonify({"message": "Usuario deleted successfully"}), 200
    else:
        return jsonify({"message": "Database connection failed"}), 500

# CRUD for bibliotecario (similar to usuario)
# CRUD for administrador (similar to usuario)
# CRUD for estoque (similar to livro but including livro_id as foreign key)
# CRUD for historico (similar to livro and usuario but including livro_id and usuario_id as foreign keys)

if __name__ == '__main__':
    app.run(debug=True)
