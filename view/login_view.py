import flet as ft

def main(page: ft.Page):
    login_view(page)

def login_view(page: ft.Page):
    page.clean()
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_maximized = True

    def go_to_register(e):
        from view import registerteste_view
        registerteste_view(page)
    
    def login_click(e):
        message_container.content = None
        if not email.value or not senha.value:
            message_container.content = ft.Text("Preencha todos os campos.", color="red")
            page.update()
            return
        # verificar_login(email.value, senha.value)
        return
    
    message_container = ft.Container(alignment=ft.alignment.center)

    email = ft.TextField(
        label='Digite o seu email',
        width=300,
        height=40,
        border_radius=40,
        prefix_icon=ft.icons.EMAIL,
        text_vertical_align=1,
        keyboard_type=ft.KeyboardType.EMAIL,
    )
    senha = ft.TextField(
        label='Digite a sua senha',
        width=300,
        height=40,
        border_radius=40,
        prefix_icon=ft.icons.LOCK,
        text_vertical_align=1,
        password=True,
        can_reveal_password=True,
        keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
    )

    Login = ft.Column([
        ft.Container(
            width=800,
            height=600,
            border_radius=10,
            content=ft.Column([
                ft.Container(
                    bgcolor=ft.colors.GREY_900,
                    width=400,
                    height=320,
                    border_radius=10,
                    content=ft.Column([
                        ft.Container(
                            padding=ft.padding.only(top=10, bottom=12),
                            content=ft.Column([
                                ft.Text(
                                    value='Login',
                                    weight='bold',
                                    size=20
                                )
                            ])
                        ),
                        ft.Column([
                            email,
                            senha,
                            message_container,
                            ft.ElevatedButton(
                                text='Entrar',
                                width=300,
                                height=40,
                                on_click=login_click
                            ),
                            ft.Row([
                                ft.TextButton(
                                    text='Criar Conta',
                                    on_click=go_to_register
                                ),
                                ft.TextButton('Esqueci minha senha')
                            ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        ], spacing=12, horizontal_alignment='center'),
                    ], horizontal_alignment='center')
                )
            ], horizontal_alignment='center', alignment='center')
        )
    ])
    page.add(Login)
    page.update()

ft.app(target=login_view)
