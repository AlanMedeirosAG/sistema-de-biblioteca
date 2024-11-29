# Gerenciador de biblioteca
Um sistema simples para gerenciar livros, usuários e empréstimos.

1. Descrição:

Este projeto foi criado para facilitar a organização e o controle de empréstimos em bibliotecas. Ele permite cadastro de usuários(bibliotecários e usuários comuns), livros e gerenciar o histórico de empréstimos de forma eficiente.

2. Pré requisitos:

- Node.js v22.8.0
- Python 3.12.6
- MySQL Workbench

Esquema de tabelas:

Obs:Nome usado no esquema das tabelas no MySQL "bdgerencia"


![Captura de tela 2024-11-28 203149](https://github.com/user-attachments/assets/e32e2842-da59-4eae-9433-269fc049095f)

![Captura de tela 2024-11-28 203207](https://github.com/user-attachments/assets/b9828e3a-99c3-4a91-a3dd-d024832e47eb)

![Captura de tela 2024-11-28 203221](https://github.com/user-attachments/assets/3930923e-739d-4660-b12d-5b75b75bfd04)

2.3. Dependencias necessárias para rodar o projeto:

- **Flask**: Framework para desenvolvimento web.
- **Flet**: Biblioteca para construir interfaces gráficas.
- **Packaging**: Biblioteca para manipulação de pacotes.
- **MySQL Connector**: Conector para interagir com bancos de dados MySQL.
- **Requests**: Biblioteca para fazer requisições HTTP.
- **Werkzeug**: Ferramenta para manipulação de WSGI e servidores web.

3. Instalação:

- Baixar o arquivo "Projeto.zip" ou clonar o repositório: git clone https://github.com/AlanMedeirosAG/sistema-de-biblioteca

![Captura de tela 2024-11-29 073227](https://github.com/user-attachments/assets/fe7be053-4e11-422e-ab32-76bd53d8f4d9)

- Criar o esquema no "MySQL Workbench"

![image](https://github.com/user-attachments/assets/5a9d7115-2e93-4f17-83fb-5d76ff413b8e)

Configurações usadas no arquivo "Server.py" para criar o servidor

- Abrir a IDE de sua preferencia 

- Após isso usar o comando "pip install -r requirements.txt" para instalar as dependencias

- Rodar o arquivo "app.py" e depois "main.py"

Obs:É aceitavel usar um terminal dedicado em sua IDE para rodar o "app.py" e "main.py"
