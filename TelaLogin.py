import flet as ft
import requests
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash

def main(page: ft.Page):
    page.title = "Tela de Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    nome = ft.TextField(width=300)
    email = ft.TextField(hint_text="exemplo: joaozinho@gmail.com", width=300)
    senha = ft.TextField(hint_text="********", password=True, width=300)

    def cadastrar_click(e):
        if not email.value or not senha.value:
            page.add(ft.Text("Preencha todos os campos.", color="red"))
            return
        
        # Dados a serem enviados
        payload = {
            "nome":nome.value,
            "email": email.value,
            "senha": senha.value
        }

        # Enviar dados para o backend Flask
        try:
            response = requests.post("http://127.0.0.1:5000/usuario", json=payload)
            if response.status_code == 201:
                page.add(ft.Text("Usuário cadastrado com sucesso!", color="green"))
            else:
                page.add(ft.Text(f"Erro ao cadastrar usuário: {response.json().get('message')}", color="red"))
        except requests.RequestException as ex:
            page.add(ft.Text(f"Erro de conexão: {ex}", color="red"))

    cadastrar = ft.ElevatedButton("Cadastrar", on_click=cadastrar_click)

    page.add(ft.Column([
        ft.Row([ft.Text("Nome")]),
        ft.Row([nome]),
        ft.Row([ft.Text("Email")]),
        ft.Row([email]),
        ft.Row([ft.Text("Senha")]),
        ft.Row([senha]),
        ft.Row([cadastrar]),
    ]))

ft.app(target=main)
