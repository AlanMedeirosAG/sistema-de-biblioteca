import flet as ft

def main(page: ft.Page):
    page.title = "Tela de login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    t1 = ft.Text("Email")
    email = ft.TextField(hint_text="exemplo: joãozinho@gmail.com", width=300)

    t2 = ft.Text("Senha")
    print("Digite a senha:")
    senha = ft.TextField(hint_text="********", width=300)

    cadastrar = ft.ElevatedButton("Cadastrar")

    ft.ElevatedButton("Cadastrar")
    page.add(ft.Row([t1]))
    page.add(ft.Row([email]))
    page.add(ft.Row([t2]))
    page.add(ft.Row([senha]))
    page.add(ft.Row([cadastrar]))

ft.app(target=main)