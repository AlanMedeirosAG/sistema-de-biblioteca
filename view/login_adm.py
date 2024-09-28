import flet as ft
import requests 

def main(page: ft.Page):
    loginAdm_view(page)

def loginAdm_view(page: ft.Page):
    page.title = 'Login Administrador'
    page.clean()
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_maximized = True

    # Função para executar o login
    def login_click(e):
        message_container.content = None

        # Verifica se os campos estão preenchidos
        if not email.value or not senha.value:
            message_container.content = ft.Text("Preencha todos os campos.", color="red")
            page.update()
            return

        # Validação do formato do e-mail
        if "@" not in email.value or "." not in email.value:
            message_container.content = ft.Text("O e-mail deve ser válido (ex: exemplo@dominio.com).", color="red")
            page.update()
            return 
        
        # Pegando os valores dos campos de texto
        email_value = email.value
        senha_value = senha.value

        try:
            # Fazendo a requisição ao backend Flask
            response = requests.post("http://127.0.0.1:5000/login", json={"email": email_value, "senha": senha_value})

            # Verificando o status da resposta
            if response.status_code == 200:
                message_container.content = ft.Text("Login com sucesso", color="green")
            else:
                message_container.content = ft.Text(f"Erro no login: {response.json().get('message')}", color="red")

        except requests.RequestException as ex:
            message_container.content = ft.Text(f"Erro de conexão: {ex}", color="red")

        page.update()
    
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
                    height=350,
                    border_radius=10,
                    content=ft.Column([
                        ft.Container(
                            padding=ft.padding.only(top=10, bottom=12),
                            content=ft.Column([
                                ft.Text(
                                    value='Login Administrador',
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
                                    on_click=lambda _: page.go("/cadastro")
                                ),
                                ft.TextButton('Esqueci minha senha')
                            ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                            ft.Container(
                                content=ft.TextButton(
                                    text='Sou Usuário',
                                    on_click=lambda _: page.go("/")
                                ), 
                            margin=30, alignment=ft.alignment.bottom_right),
                        ], spacing=12, horizontal_alignment='center'),
                    ], horizontal_alignment='center')
                )
            ], horizontal_alignment='center', alignment='center')
        )
    ])
    return ft.View(
        "/loginadm",
        [
            Login,
        ],
        horizontal_alignment='center'
    )
