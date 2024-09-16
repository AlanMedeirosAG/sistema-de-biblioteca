import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_maximized = True

    Login = ft.Column([
        ft.Container(
            width = page.window.width - 10,
            height = page.window.height - 60,
            border_radius = 10,
            content = ft.Column([
                ft.Container(
                    bgcolor = ft.colors.GREY_900,
                    width = 400,
                    height = 320,
                    border_radius = 10,

                    content=ft.Column([
                        ft.Container( 
                            padding = ft.padding.only(
                                top=10,
                                bottom = 12
                            ),
                            content = ft.Column([
                                ft.Text(
                                    value='Login',
                                    weight='bold',
                                    size=20
                                )
                            ])
                        ),

                        ft.Column([
                            ft.TextField(
                                hint_text='Digite o seu email',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.EMAIL,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.EMAIL,
                            ),
                            ft.TextField(
                                hint_text='Digite a sua senha',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                text_vertical_align=1,
                                password=True,
                                can_reveal_password=True,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                            ),
                            ft.ElevatedButton(
                                text='Entrar',
                                width=150,
                                height=40
                            ),
                            ft.Row([
                                ft.TextButton(text='Criar Conta'),
                                ft.TextButton('Esqueci minha senha')
                            ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        ],spacing=12),

                        ft.Row([
                            ft.IconButton(icon=ft.icons.EMAIL),
                            ft.IconButton(icon=ft.icons.FACEBOOK),
                            ft.IconButton(icon=ft.icons.TELEGRAM)
                        ], alignment='center')
                    ], horizontal_alignment='center')
                )
            ], horizontal_alignment= 'center', alignment='center')
        )
    ])
    page.add(Login)

ft.app(target=main)