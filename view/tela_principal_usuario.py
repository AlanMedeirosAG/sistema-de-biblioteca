import flet as ft

def main(page: ft.Page):
    tela_principal_usuario_view(page)
    
def tela_principal_usuario_view(page: ft.Page):
    page.title = 'Principal Usuário'
    page.clean()
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_maximized = True
    def show_search_dialog(e):
        search_field = ft.TextField(label="Buscar Livros", expand=True)
        
        def close_dialog(e):
            page.dialog.open = False
            page.update()

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Pesquisar Livros"),
            content=ft.Column(
                controls=[
                    search_field
                ],
                tight=True
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dialog),
                ft.TextButton("Pesquisar", on_click=lambda e: print(f"Buscando: {search_field.value}")),
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

        page.dialog = dialog
        dialog.open = True
        page.update()

    tela_principal_usuario = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                icon=ft.icons.SEARCH,
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                             ft.Row(
                                controls=[
                                    ft.TextField(
                                        label="Digite o titulo do livro que você deseja encontrar", 
                                        expand=True
                                    ),
                                    ft.IconButton(
                                        icon="search"
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.START,
                                spacing=10
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10
                    ),
                    alignment=ft.alignment.top_left,
                    padding=ft.padding.all(10)
                ),
            ),
            ft.Tab(
                text="Início",
                icon=ft.icons.HOME,
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Bem-vindo à Biblioteca!"),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10
                    ),
                    alignment=ft.alignment.top_left,
                    padding=ft.padding.all(10)
                ),
            ),
            ft.Tab(
                text="Explorar",
                icon=ft.icons.EXPLORE,
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Explore nossos gêneros e descubra novos títulos."),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10
                    ),
                    alignment=ft.alignment.top_left,
                    padding=ft.padding.all(10)
                ),
            ),
            ft.Tab(
                text="Meus Empréstimos",
                icon=ft.icons.LIBRARY_BOOKS,
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Seus emprestimos:"),
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Text("Título: As Crônicas de Gelo e Fogo, Volume 1"),
                                            ft.Text("Data de Empréstimo: 01/09/2024"),
                                            ft.Text("Data de Devolução: 15/09/2024"),
                                        ],
                                        spacing=5
                                    ),
                                    padding=ft.padding.all(10),
                                ),
                                elevation=4,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10
                    ),
                    alignment=ft.alignment.top_left,
                    padding=ft.padding.all(10)
                ),
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
                                        text="Dados de Usuario", 
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
            ),
        ],
        expand=1
    )

    page.add(tela_principal_usuario)

    return ft.View(
        "/tela_principal_usuario",
        [
            tela_principal_usuario,
        ],
        horizontal_alignment='center'
    )
