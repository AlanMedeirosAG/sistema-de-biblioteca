import flet as ft

# Função para atualizar a tela com o conteúdo da página 'for.py'
def pagina_login(page: ft.Page):
    page.clean()  # Limpa a tela atual
    page.add(ft.Text("Bem-vindo à página de login!"))  # Exemplo de conteúdo
    page.update()  # Atualiza a página com o novo conteúdo
