from datetime import datetime
import flet as ft
from flet import ListView
import requests 

def main(page: ft.Page):
    tela_principal_bibliotecario_view(page)
    
def tela_principal_bibliotecario_view(page: ft.Page):
    page.title = 'Principal Bibliotecario'
    page.clean()
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_maximized = True

    # Lista para armazenar os livros adicionados
    livros = []
    historicos = []
    
    message_container = ft.Container(content=ft.Text("Aguardando ação..."))

    # Função para buscar os livros do banco de dados
    def carregar_livros():
        try:
            # Fazendo a requisição ao backend Flask para buscar os livros
            response = requests.get("http://127.0.0.1:5000/livro")
            if response.status_code == 200:
                
                livros_backend = response.json()  # Obtém a lista de livros

                if isinstance(livros_backend, list): # Verifica se é uma lista
                    livros.clear()
                    for livro in livros_backend:
                        livro_dict = {
                            "idlivro": livro[0],         
                            "titulo": livro[1], 
                            "autor": livro[2],     
                            "isbn": livro[3],
                            "genero": livro[4],     
                            "quantidade": livro[6] 
                        }

                        livros.append(livro_dict)  # Adiciona o dicionário à lista de livros    
                    atualizar_lista_de_livros(livros)  # Atualiza a interface com os livros obtidos
                else:
                    message_container.content = ft.Text("Erro: O formato dos dados retornados não é uma lista.", color="red")
            else:
                message_container.content = ft.Text(f"Erro ao carregar livros: {response.json().get('message')}", color="red")
        except requests.RequestException as ex:
            message_container.content = ft.Text(f"Erro de conexão: {ex}", color="red")
        page.update()
        
    #Função de carregar historicos
    def carregar_historicos():
        try:
            # Fazendo a requisição ao backend Flask para buscar os livros
            response = requests.get("http://127.0.0.1:5000/historico")
            if response.status_code == 200:
                
                historicos_backend = response.json()  # Obtém a lista de historicos
                
                print("Dados recebidos do backend:", historicos_backend)
            
                if isinstance(historicos_backend, list): # Verifica se é uma lista
                    historicos.clear()
                    for historico in historicos_backend:
                        historico_dict = {
                            "idhistorico": historico["idhistorico"],         
                            "livro": historico["livro"],
                            "multa": historico["multa"],
                            "data_emprestimo": historico["data_emprestimo"],
                            "data_devolucao": historico["data_devolucao"],     
                            "idusuario": historico["idusuario"],
                            "devolvido": historico["devolvido"]
                        }

                        historicos.append(historico_dict) # Adiciona o dicionário à lista de livros
                    print("Históricos carregados:", historicos)
                    atualizar_lista_historicos()  # Atualiza a interface com os livros obtidos
                else:
                    message_container.content = ft.Text("Erro: O formato dos dados retornados não é uma lista.", color="red")
            else:
                message_container.content = ft.Text(f"Erro ao carregar historicos: {response.json().get('message')}", color="red")
        except requests.RequestException as ex:
            message_container.content = ft.Text(f"Erro de conexão: {ex}", color="red")
        page.update()
        

    #Função de excluir livros
    def excluirLivro(id):
        try:
            # Fazendo a requisição ao backend Flask para apagar livro
            response = requests.delete(f"http://127.0.0.1:5000/livro/{id}")
            if response.status_code == 200:
                    message_container.content = ft.Text("Livro excluído com sucesso!", color="green")
                    carregar_livros()
                    atualizar_lista_de_livros()
            else:
                message_container.content = ft.Text(f"Erro ao excluir livro: {response.json().get('message')}", color="red")
        except requests.RequestException as ex:
            message_container.content = ft.Text(f"Erro de conexão: {ex}", color="red")
        page.update()

    #pesquisa o livro por nome ou id e verifica se a quantidade de livros é maior que zero para o emprestimo
    def pesquisaLivro(id=None, titulo=None):
        try:
            # Verifica se o ID ou o título foi fornecido
            if id:
                response = requests.get(f"http://127.0.0.1:5000/livro?idlivro={id}")
            elif titulo:
                response = requests.get(f"http://127.0.0.1:5000/livro?titulo={titulo}")
            else:
                print("É necessário fornecer o ID ou o nome do livro.")
                message_container.content = ft.Text("É necessário fornecer o ID ou o nome do livro.", color="red")
                return None

            # Verifica se a requisição foi bem-sucedida
            if response.status_code == 200:
                livro_data = response.json()  # Converte a resposta JSON para um dicionário
                return livro_data
            else:
                print(f"Erro ao buscar o livro. Status code: {response.status_code}")
                return None

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            message_container.content = ft.Text(f"Ocorreu um erro: {e}", color="red")
            return None


    def pesquisaUsuario(email=None, nome=None):
        try:
            # Verifica se o e-mail ou o nome foi fornecido
            if email:
                response = requests.get(f"http://127.0.0.1:5000/usuario?email={email}")
            elif nome:
                response = requests.get(f"http://127.0.0.1:5000/usuario?nome={nome}")
            else:
                print("É necessário fornecer o e-mail ou o nome do usuário.")
                return None

                # Verifica se a requisição foi bem-sucedida
            if response.status_code == 200:
                usuario_data = response.json()  # Converte a resposta JSON para um dicionário
            
                if usuario_data:  # Verifica se há dados do usuário
                    print("Usuário encontrado:")
                    print(usuario_data)  # Imprime os dados do usuário encontrado
                    return usuario_data  # Retorna os dados do usuário
                else:
                    print("Usuário não encontrado.")  # Mensagem se não houver dados
                    return None
            else:
                print(f"Erro ao buscar o usuário. Status code: {response.status_code}")
                return None

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return None

    # Função para atualizar a exibição da lista de livros na tela
    def atualizar_lista_de_livros(livros_exibir=None):
        print("livros a exibir:",livros_exibir)
    # Limpa os elementos atuais e insere os livros da lista
        lista_livros_coluna.controls.clear()
        lista_para_mostrar = livros_exibir if livros_exibir is not None else livros

        for livro in lista_para_mostrar:
            print(livro)
            if isinstance(livro, dict) and all(key in livro for key in ['titulo', 'autor', 'genero', 'isbn', 'idlivro', 'quantidade']):
                lista_livros_coluna.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Column(
                                            controls=[
                                                ft.Text(f"Título: {livro['titulo']}"),
                                                ft.Text(f"Autor: {livro['autor']}"),
                                                ft.Text(f"Gênero: {livro['genero']}"),
                                                ft.Text(f"ISBN: {livro['isbn']}"),
                                                ft.Text(f"ID: {livro['idlivro']}"),
                                                ft.Text(f"Quantidade: {livro['quantidade']}"),
                                            ],
                                            spacing=5
                                        ),
                                    ],
                                    spacing=10 
                                ),
                                ft.Row(
                                    controls=[
                                        ft.TextButton(text='Editar Detalhes'),
                                        ft.TextButton(text='Excluir livro',on_click=lambda e, livro_id=livro['idlivro']: excluirLivro(livro_id))
                                        ],
                                    alignment=ft.MainAxisAlignment.END,
                                    spacing=10
                                )
                            ],
                            spacing=10
                        ),
                        padding=ft.padding.all(10),
                    ),
                    width=800,
                    elevation=4
                )
            )
            else:
                 lista_livros_coluna.controls.append(
                ft.Text("Erro: Livro com dados inválidos.", color='red')
            )
        page.update()
    
    # Função para atualizar a exibição da lista de historico na tela
    def atualizar_lista_historicos():
        # Limpa os elementos atuais e insere os livros da lista
        lista_historicos_coluna.controls.clear()

        for historico in historicos:
            lista_historicos_coluna.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Column(
                                            controls=[
                                                ft.Text(f"Usuário: {historico['idusuario']}"),
                                                ft.Text(f"Livro: {historico['livro']}"),
                                                ft.Text(f"Data de Empréstimo: {historico['data_emprestimo']}"),
                                                ft.Text(f"Data de Devolução: {historico['data_devolucao']}"),
                                                ft.Text(f"Empréstimo ID: {historico['idhistorico']}"),
                                                ft.Text(f"Multa: {historico['multa']} R$"),
                                            ],
                                            spacing=5
                                        ),
                                    ],
                                    spacing=10 
                                ),
                                ft.Row(
                                    controls=[
                                        ft.TextButton(
                                            text="Devolvido" if historico['devolvido'] else "Devolver livro",
                                            on_click=lambda e, emprestimo_id=historico['idhistorico'], livro=historico['livro']: book_return(
                                            idhistorico=emprestimo_id, 
                                            livro=livro, 
                                            button=e.control
                                            ),
                                            disabled=historico['devolvido'])

                                    ],
                                    alignment=ft.MainAxisAlignment.END,
                                    spacing=10
                                )
                            ],
                            spacing=10
                        ),
                        padding=ft.padding.all(10),
                    ),
                    width=800,
                    elevation=4
                )
            )
            page.update()

    # Função de tela de empréstimo
    def show_add_loan_dialog(e):
        usuario = ft.TextField(label="Nome ou Email", width=400)
        livro = ft.TextField(label="Título ou ID do livro", width=400)
        data_emprestimo = ft.TextField(label="Data de Empréstimo (YYYY-MM-DD)", width=400)
        data_devolucao = ft.TextField(label="Data de Devolução (YYYY-MM-DD)", width=400)

        message_container = ft.Text(color="red")  # Contêiner para mensagens de validação

        def close_dialog(e):
            page.dialog.open = False
            page.update()

        # Função para validar data no formato YYYY-MM-DD
        def validar_data(data_texto):
            try:
                datetime.strptime(data_texto, "%Y-%m-%d").date()
                return True
            except ValueError:
                return False

        # Função para salvar os dados do novo empréstimo
        def add_loan(e):
            message_container.value = ""  # Limpa mensagens anteriores
            usuario_nome_email = usuario.value
            livro_titulo_id = livro.value
            data_emp = data_emprestimo.value
            data_dev = data_devolucao.value

            # Validação dos campos
            if not usuario_nome_email or not livro_titulo_id or not data_emp or not data_dev:
                message_container.value = "Todos os campos são obrigatórios."
                page.update()
                return

            if not (validar_data(data_emp) and validar_data(data_dev)):
                message_container.value = "Datas devem estar no formato YYYY-MM-DD."
                page.update()
                return

            # Formatar as datas para garantir que seja apenas YYYY-MM-DD
            data_emp_formatada = datetime.strptime(data_emp, "%Y-%m-%d").date().strftime("%Y-%m-%d")
            data_dev_formatada = datetime.strptime(data_dev, "%Y-%m-%d").date().strftime("%Y-%m-%d")

            # Criação do objeto de dados para o empréstimo
            emprestimo_data = {
                "usuario": usuario_nome_email,
                "livro": livro_titulo_id,
                "data_emprestimo": data_emp_formatada,
                "data_devolucao": data_dev_formatada,
            }

            # Envio dos dados para o backend
            try:
                response = requests.post("http://127.0.0.1:5000/emprestimo", json=emprestimo_data)
                if response.status_code == 201:
                    message_container.value = "Empréstimo adicionado com sucesso!"
                    message_container.color = "green"

                    carregar_historicos()
                    carregar_livros()

                    close_dialog(e)  # Fecha o diálogo após o sucesso
                else:
                    message_container.value = "Erro ao adicionar empréstimo. Tente novamente."
                    message_container.color = "red"
            except Exception as ex:
                message_container.value = f"Ocorreu um erro: {ex}"
                message_container.color = "red"
            page.update()

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Adicionar Novo Empréstimo"),
            content=ft.Column(
                controls=[
                    usuario,
                    livro,
                    data_emprestimo,
                    data_devolucao,
                    message_container  # Exibe a mensagem de erro ou sucesso
                ],
            tight=True
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dialog),
                ft.TextButton("Adicionar", on_click=add_loan),
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

        page.dialog = dialog
        dialog.open = True
        page.update()

        
    #Função de devolução de livros
    def book_return(idhistorico, livro, button):
        
        try:
            
            print(idhistorico)
            print(livro)
 
            # Enviar o livro como dicionário contendo 'id' ou 'titulo'
            if isinstance(livro, int):  # Se 'livro' for um ID
                livro_info = {'idlivro': livro}
            elif isinstance(livro, str):  # Se 'livro' for um título
                livro_info = {'livro': livro}
            else:
                livro_info = livro  # Se já for um dicionário

            devolucao_data = {
                "idhistorico": idhistorico,
                "livro": livro_info  # Passa 'livro' como um dicionário
            }

            response = requests.put("http://127.0.0.1:5000/emprestimo", json=devolucao_data)

            if response.status_code == 200:
                print("Livro devolvido com sucesso!")
            
                # Atualiza o botão na interface
                button.text = "Devolvido"
                button.enabled = False
                button.on_click = None
                button.update()

                # Atualiza a lista de livros
                carregar_livros()
            else:
                print("Erro ao devolver o livro.")
                print(f"Erro: {response.json().get('message', 'Erro desconhecido')}")

        except Exception as ex:
            print(f"Ocorreu um erro: {ex}")



    #Função de tela de adição de livros no estoque
    def show_add_book_dialog(e):
        # Definindo os TextFields para a entrada do usuário
        titulo_livro = ft.TextField(label="Título do Livro", width=400)
        genero = ft.TextField(label="Gênero", width=400)
        autor_livro = ft.TextField(label="Autor", width=400)
        isbn = ft.TextField(label="isbn",width=400)

        # Definindo um campo de número para a quantidade e inicializando o valor
        quantidade_de_livros = ft.TextField(
            label="Quantidade", 
            value="1", 
            width=100, 
            text_align=ft.TextAlign.CENTER
        )

        # Função para aumentar a quantidade
        def aumentar_quantidade(e):
            quantidade_de_livros.value = str(int(quantidade_de_livros.value) + 1)
            page.update()

        # Função para diminuir a quantidade
        def diminuir_quantidade(e):
            if int(quantidade_de_livros.value) > 1:
                quantidade_de_livros.value = str(int(quantidade_de_livros.value) - 1)
                page.update()

        # Função para fechar o diálogo
        def close_dialog(e):
         page.dialog.open = False
         page.update()

        # Função para salvar os dados do novo livro
        def add_book(e):
            message_container.content = None

            # Criando um dicionário com as informações do livro
            novo_livro = {
                "titulo": titulo_livro.value,
                "autor": autor_livro.value,
                "genero": genero.value,
                "quantidade": quantidade_de_livros.value,
                "isbn":isbn.value
            }

            if not all(novo_livro.values()):
                message_container.content = ft.Text("Por favor, preencha todos os campos obrigatórios.", color="red")
                page.update()
                return

            try:
                # Fazendo a requisição ao backend Flask
                response = requests.post("http://127.0.0.1:5000/livro", json=novo_livro)

                # Verificando o status da resposta
                if response.status_code == 201:
                    idlivro = response.json().get('idlivro')  # Obtém o ID do livro retornado
                    novo_livro['idlivro'] = idlivro  # Adiciona o ID ao dicionário
                    livros.append(novo_livro)  # Adiciona o livro à lista
                    atualizar_lista_de_livros()# Atualiza a interface com a lista atualizada
                    carregar_livros()

                    message_container.content = ft.Text("Livro adicionado com sucesso", color="green")
                else:
                    message_container.content = ft.Text(f"Erro ao adicionar livro: {response.json().get('message')}", color="red")

            except requests.RequestException as ex:
                message_container.content = ft.Text(f"Erro de conexão: {ex}", color="red")

            close_dialog(e)

        # Função para simular a escolha de arquivo ou tirar foto
        def tirar_foto(e):
            print("Tirando uma foto...")
            page.update()

        def escolher_arquivo(e):
            print("Escolhendo arquivo de imagem...")
            page.update()

        # Criando a caixa de diálogo
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Adicionar Novo Livro"),
            content=ft.Column(
                controls=[
                    ft.Text("Adicione a capa do livro"),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="Tirar Foto",
                                icon=ft.icons.CAMERA,
                                on_click=tirar_foto
                            ),
                            ft.ElevatedButton(
                                text="Escolher Arquivo",
                                icon=ft.icons.ATTACH_FILE,
                                on_click=escolher_arquivo
                            ),
                        ],
                        spacing=10
                    ),

                    titulo_livro,
                    genero,
                    autor_livro,
                    isbn,
                    ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.REMOVE,
                                on_click=diminuir_quantidade
                            ),
                            quantidade_de_livros,
                            ft.IconButton(
                                icon=ft.icons.ADD,
                                on_click=aumentar_quantidade
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=5
                    ),
                ],
                tight=True
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dialog),
                ft.TextButton("Adicionar", on_click=add_book),
            ],
            actions_alignment=ft.MainAxisAlignment.END
          )
 
         # Mostrando o diálogo
        page.dialog = dialog
        dialog.open = True
        page.update()


    # Coluna para listar os livros
    lista_livros_coluna = ft.ListView(
        controls=[],  
        expand=True,  
        spacing=10,   
        padding=ft.padding.all(10),
        auto_scroll=True  
    )

    lista_historicos_coluna = ft.ListView(
        controls=[],  
        expand=True,
        spacing=10,
        padding=ft.padding.all(10),
        auto_scroll=True  
    )

    
    # Pesquisa de livro
    def on_search(e):
        # Pega o valor do campo de texto
        campo = search_field.value.strip()
    
        # Chama a função de pesquisa
        resultado = pesquisaLivro(titulo=campo)

        # Verifica se o resultado é uma lista de listas
        if isinstance(resultado, list) and all(isinstance(item, list) for item in resultado):
        # Converte listas em dicionários
            resultado = [
                {
                    'idlivro': item[0],
                    'titulo': item[1],
                    'autor': item[2],
                    'isbn': item[3],
                    'genero': item[4],
                    'quantidade': item[6],
                }
                for item in resultado
            ]

        # Atualiza a interface com os resultados
        if resultado:
            atualizar_lista_de_livros(resultado)  # Passa diretamente resultado
            result_text.value = "Livros encontrados"
        else:
            result_text.value = "Por favor digite um titulo para pesquisar"
            atualizar_lista_de_livros(livros)

        # Atualiza a interface
    page.update()

    search_field = ft.TextField(label="Buscar no estoque", 
        expand=True,
        on_change=None,
        )
    result_text = ft.Text(value="", size=20)
    
    

    # Parte visual da tela de bibliotecário
    tela_principal_bibliotecario = ft.Tabs(
    selected_index=1,
    animation_duration=300,
    tabs=[
        ft.Tab(
            text="Estoque de Livros",
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                search_field,
                                ft.IconButton(
                                    icon="search",
                                    on_click=on_search,  # pesquisa de livros pelo icone da lupa
                                )
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            spacing=10
                        ),
                        ft.ElevatedButton(
                            text="Adicionar Novo Livro",
                            icon="add",
                            height=50,
                            width=300,
                            on_click=show_add_book_dialog
                        ),
                        lista_livros_coluna  # Exibe a lista de livros aqui
                    ],
                    alignment=ft.alignment.top_left,
                    spacing=10
                ),
                alignment=ft.alignment.top_left,
                padding=ft.padding.all(10)
            ),
            icon=ft.icons.BOOK
        ),
        ft.Tab(
            text="Histórico de Empréstimos",
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.TextField(
                                    label="Buscar usuários", 
                                    expand=True
                                ),
                                ft.IconButton(
                                    icon="search"
                                )
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            spacing=10
                        ),
                        ft.ElevatedButton(
                            text="Adicionar Novo Empréstimo",
                            icon="add",
                            height=50,
                            width=300,
                            on_click=show_add_loan_dialog
                        ),
                        lista_historicos_coluna  # Exibe a lista de históricos aqui
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10
                ),
                alignment=ft.alignment.top_left,
                padding=ft.padding.all(10)
            ),
            icon=ft.icons.PERSON
        ),
        ft.Tab(
            text="Configurações",
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Configurações Gerais"),
                        ft.Switch(label="Notificações"),
                        ft.Switch(label="Modo Escuro"),
                        ft.TextButton(text="Redefinir Configurações", on_click=lambda e: print("Configurações Redefinidas")),
                        ft.Text("Configurações de Usuário"),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    text="Dados de Bibliotecário", 
                                    expand=True, 
                                    icon="Person",
                                    icon_color="white",
                                    color="white",
                                    height=60,
                                    style=ft.ButtonStyle(
                                        alignment=ft.alignment.center_left,
                                        shape=ft.RoundedRectangleBorder(radius=0)
                                    )
                                )
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    text="Editar Perfil", 
                                    expand=True, 
                                    icon="Edit",
                                    icon_color="white",
                                    color="white",
                                    height=60,
                                    style=ft.ButtonStyle(
                                        alignment=ft.alignment.center_left,
                                        shape=ft.RoundedRectangleBorder(radius=0)
                                    )
                                )
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    text="Alterar Senha", 
                                    expand=True, 
                                    icon="Lock",
                                    icon_color="white",
                                    color="white",
                                    height=60,
                                    style=ft.ButtonStyle(
                                        alignment=ft.alignment.center_left,
                                        shape=ft.RoundedRectangleBorder(radius=0)
                                    )
                                )
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    text="Política de Privacidade e Termos de Uso", 
                                    expand=True, 
                                    icon="Menu_book",
                                    icon_color="white",
                                    color="white",
                                    height=60,
                                    style=ft.ButtonStyle(
                                        alignment=ft.alignment.center_left,
                                        shape=ft.RoundedRectangleBorder(radius=0)
                                    )
                                )
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    text="Excluir Conta", 
                                    expand=True, 
                                    icon="HIGHLIGHT_REMOVE",
                                    icon_color="red",
                                    color="red",
                                    height=60,
                                    style=ft.ButtonStyle(
                                        alignment=ft.alignment.center_left,
                                        shape=ft.RoundedRectangleBorder(radius=0)
                                    )
                                )
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.CupertinoButton(
                                    text="Sair da Conta", 
                                    color="red"
                                )
                            ]
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10
                ),
                alignment=ft.alignment.top_left,
                padding=ft.padding.all(10)
            ),
            icon=ft.icons.SETTINGS,
        )
    ],
    expand=1
    )
    page.add(tela_principal_bibliotecario)
    carregar_livros() #carrega os livros ao iniciar a tela
    carregar_historicos() #carrega os emprestimos na tela
    page.update()

    return ft.View(
        "/tela_principal_bibliotecario",
        [
            tela_principal_bibliotecario,
        ],
        horizontal_alignment='center'
    )   
