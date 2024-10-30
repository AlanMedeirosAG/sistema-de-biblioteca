from flask import Flask
from controller.controllers_usuario import usuario_bp
from controller.controllers_bibliotecario import bibliotecario_bp
from controller.controllers_administrador import administrador_bp
from controller.controllers_livro import livro_bp
from controller.controllers_historico import historico_bp
from controller.controllers_emprestimo import emprestimo_bp

#Definição do app Flask
app = Flask(__name__)

# Registrar os Blueprints
app.register_blueprint(usuario_bp)
app.register_blueprint(bibliotecario_bp)
app.register_blueprint(administrador_bp)
app.register_blueprint(livro_bp)
app.register_blueprint(historico_bp)
app.register_blueprint(emprestimo_bp)

#Roda o app
if __name__ == '__main__':
    app.run(debug=True)
