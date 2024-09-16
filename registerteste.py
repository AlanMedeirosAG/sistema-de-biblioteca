import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_maximized = True

    background = ft.Container(
        width=page.window.width,
        height=page.window.height,
        opacity=0.8,
        content=None,
        image_src='Downloads\estante.jpg',
        image_fit=ft.ImageFit.COVER 
    )

    registerUsr = ft.Column([
        ft.Container(
            width = page.window.width - 10,
            height = page.window.height - 10,
            border_radius = 10,
            content = ft.Column([
                ft.Container(
                    bgcolor = ft.colors.GREY_900,
                    width = 400,
                    height = 430,
                    border_radius = 10,

                    content=ft.Column([
                        ft.Container( 
                            padding = ft.padding.only(
                                top= 10,
                                bottom = 12
                            ),
                            content = ft.Column([
                                ft.Text(
                                    value='Cadastro',
                                    weight='bold',
                                    size=20
                                )
                            ])
                        ),

                        ft.Column([
                            ft.TextField(
                                hint_text='Digite o seu nome',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PERSON,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.NAME,
                            ),
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
                            ft.TextField(
                                hint_text='Confirme sua senha',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                text_vertical_align=1,
                                password=True,
                                can_reveal_password=True,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                            ),
                                ft.TextField(
                                hint_text='Digite o seu telefone',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PHONE,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.PHONE,
                            ),
                            ft.ElevatedButton(
                                text='Criar conta',
                                width=300,
                                height=40
                            ),
                            ft.Row([
                                ft.TextButton('Já tenho uma conta'),
                            ], width=300)
                        ],spacing=12),
                    ], horizontal_alignment='center'),
                )
            ], horizontal_alignment= 'center', alignment='center'),
        )
    ])
    page.add(
        ft.Stack(
            [
                background,
                ft.Container(
                    content=registerUsr,
                    alignment=ft.alignment.center
                )
            ]
        )
    )


ft.app(target=main)