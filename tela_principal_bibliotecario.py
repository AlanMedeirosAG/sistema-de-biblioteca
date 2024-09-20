import flet as ft

def main(page: ft.Page):
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
                                label="Qual livro você quer buscar hoje?", # Ajuste a altura do TextField se necessário
                                expand=True

                            ),
                            ft.IconButton(
                                icon="search"
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10  # Espaçamento entre o TextField e o IconButton
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
                                height=50, 
                                width=300,
                            ),
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                controls=[
                                                    ft.Image(
                                                        src="https://m.media-amazon.com/images/I/91+1SUO3vUL._AC_UF1000,1000_QL80_.jpg",
                                                        width=100,  # Ajuste o tamanho da imagem
                                                        height=150  # Ajuste o tamanho da imagem
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
                                                spacing=10  # Espaçamento entre a imagem e o texto
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
                        spacing=10  # Espaçamento entre o botão e o card
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

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
