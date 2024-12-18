import flet as ft
import requests
from werkzeug.security import generate_password_hash

def register_view(page: ft.Page):
    page.clean()
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_maximized = True

    # Campos de entrada
    nome = ft.TextField(label='Digite o seu nome', width=300, height=40, border_radius=40, prefix_icon=ft.icons.PERSON)
    email = ft.TextField(label='Digite o seu email', width=300, height=40, border_radius=40, prefix_icon=ft.icons.EMAIL)
    senha = ft.TextField(label='Digite a sua senha', width=300, height=40, border_radius=40, prefix_icon=ft.icons.LOCK, password=True, can_reveal_password=True)
    senhaconfirm = ft.TextField(label='Confirme sua senha', width=300, height=40, border_radius=40, prefix_icon=ft.icons.LOCK, password=True, can_reveal_password=True)

    tipo_usuario = ft.Dropdown(label="Tipo de conta", options=[
        ft.dropdown.Option(key="usuario", text="Usuário Comum"),
        ft.dropdown.Option(key="bibliotecario", text="Bibliotecário"),
    ], value="usuario", width=300)

    message_container = ft.Container(alignment=ft.alignment.center)

    #Função que controla o registro
    def cadastrar_click(e):

        #verifica se os dados inseridos são validos
        message_container.content = None
        if not nome.value or not email.value or not senha.value or not senhaconfirm.value:
            message_container.content = ft.Text("Preencha todos os campos.", color="red")
            page.update()
            return
        if senha.value != senhaconfirm.value:
            message_container.content = ft.Text("Senhas não conferem.", color="red")
            page.update()
            return

        if "@" not in email.value or "." not in email.value:
            message_container.content = ft.Text("O e-mail deve ser válido (ex: exemplo@dominio.com).", color="red")
            page.update()
            return

        hashed_password = generate_password_hash(senha.value)

        # Dados a serem enviados
        payload = {
            "nome": nome.value,
            "email": email.value,
            "senha": hashed_password,
            "tipo_usuario": tipo_usuario.value  # Enviar o tipo de usuário
        }

        # Enviar dados para o backend Flask
        try:
            response = requests.post("http://127.0.0.1:5000/usuario", json=payload)

            if response.status_code == 201:
                message_container.content = ft.Text("Usuário cadastrado com sucesso!", color="green")
            else:
                message_container.content = ft.Text(f"Erro ao cadastrar usuário: {response.json().get('message')}", color="red")
        except requests.RequestException as ex:
            message_container.content = ft.Text(f"Erro de conexão: {ex}", color="red")

        page.update()

    #Parte visual da tela de registro
    registerUsr = ft.Column([
        ft.Container(
            width=800,
            height=600,
            border_radius=10,
            content=ft.Column([
                ft.Container(
                    bgcolor=ft.colors.GREY_900,
                    width=400,
                    height=460,
                    border_radius=10,
                    content=ft.Column([
                        ft.Container(
                            padding=ft.padding.only(top=10, bottom=12),
                            content=ft.Text(value='Cadastro', weight='bold', size=20)
                        ),
                        ft.Column([
                            nome, email, senha, senhaconfirm, tipo_usuario,
                            ft.ElevatedButton(on_click=cadastrar_click, text='Criar conta', width=300, height=40),
                            message_container,
                            ft.Row([ft.TextButton(text='Já tenho uma conta', on_click=lambda _: page.go("/"))], width=300)
                        ], spacing=12, horizontal_alignment='center'),
                    ], horizontal_alignment='center'),
                )
            ], horizontal_alignment='center', alignment='center'),
        )
    ])

    return ft.View("/cadastro", [registerUsr], horizontal_alignment='center')
