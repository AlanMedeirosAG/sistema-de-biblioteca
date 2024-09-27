import flet as ft

def main(page: ft.Page):
    def show_add_book_dialog(e):
        # Definindo os TextFields para a entrada do usuário (removido expand=True)
        titulo_livro = ft.TextField(label="Título do Livro", width=400)
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
            print(f"Título: {titulo_livro.value}, Autor: {autor_livro.value}, Quantidade: {quantidade_de_livros.value}")
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

    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                tab_content=ft.Icon(ft.icons.SEARCH),
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.TextField(
                                label="Qual livro você quer buscar hoje?", 
                                expand=True
                            ),
                            ft.IconButton(
                                icon="search"
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10
                    ),
                    alignment=ft.alignment.top_left,
                    padding=ft.padding.all(10)
                ),
            ),
            ft.Tab(
                text="Estoque de Livros",
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.ElevatedButton(
                                text="Adicionar Novo Livro",
                                icon="add",
                                height=50,
                                width=300,
                                on_click=show_add_book_dialog
                            ),
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                controls=[
                                                    ft.Image(
                                                        src="https://m.media-amazon.com/images/I/91+1SUO3vUL._AC_UF1000,1000_QL80_.jpg",
                                                        width=100,
                                                        height=150
                                                    ),
                                                    ft.Column(
                                                        controls=[
                                                            ft.Text("As crônicas de Gelo e Fogo"),
                                                            ft.Text("Autor: George R.R. Martin"),
                                                            ft.Text("Quantidade: 300"),
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
                        ],
                        alignment=ft.alignment.top_left,
                        spacing=10
                    ),
                    alignment=ft.alignment.top_left,
                    padding=ft.padding.all(10)
                ),
            ),
            ft.Tab(
                text="Histórico de Usuários",
                icon=ft.icons.SETTINGS,
            ),
        ],
        expand=1
    )

    page.add(t)

ft.app(target=main)
