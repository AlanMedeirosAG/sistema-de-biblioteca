import flet as ft

def main(page: ft.Page):
    # Lista para armazenar os livros adicionados
    livros = []

    def show_add_book_dialog(e):
        # Definindo os TextFields para a entrada do usuário
        titulo_livro = ft.TextField(label="Título do Livro", width=400)
        genero = ft.TextField(label="Gênero", width=400)
        autor_livro = ft.TextField(label="Autor", width=400)

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
            # Criando um dicionário com as informações do livro
            novo_livro = {
                "titulo": titulo_livro.value,
                "autor": autor_livro.value,
                "genero": genero.value,
                "quantidade": quantidade_de_livros.value
            }
            livros.append(novo_livro)  # Adiciona o livro à lista
            atualizar_lista_de_livros()  # Atualiza a interface com a lista atualizada
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

    # Função para atualizar a exibição da lista de livros na tela
    def atualizar_lista_de_livros():
        # Limpa os elementos atuais e insere os livros da lista
        lista_livros_coluna.controls.clear()
        for livro in livros:
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
                                        ft.TextButton(text='Adicionar mais unidades ao catálogo'),
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

    # Coluna para listar os livros
    lista_livros_coluna = ft.Column()

    t = ft.Tabs(
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
                                    ft.TextField(
                                        label="Buscar no estoque",
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
                                on_click=lambda e: print("Adicionar Novo Empréstimo")
                            ),
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

    page.add(t)

ft.app(target=main)
