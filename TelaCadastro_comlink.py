import flet as ft
from pagina_login import pagina_login  # Certifique-se de que o nome do arquivo esteja correto

def main(page: ft.Page):
    page.title = "Tela de cadastro"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    t1 = ft.Text("Email")
    email = ft.TextField(hint_text="exemplo: joaozinho@gmail.com", width=300)

    t2 = ft.Text("Senha")
    senha = ft.TextField(hint_text="********", password=True, width=300)

    def cadastrar_usuario(e):
        # Atualiza a tela atual para o conteúdo da página 'for.py'
        pagina_login(page)  # Chama a função de 'for.py' que atualiza a página

    # Adiciona componentes na tela
    page.add(ft.Row([t1]))
    page.add(ft.Row([email]))
    page.add(ft.Row([t2]))
    page.add(ft.Row([senha]))
    page.add(ft.ElevatedButton("Cadastrar", on_click=cadastrar_usuario))

    page.update()

ft.app(target=main)
