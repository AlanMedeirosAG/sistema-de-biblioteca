import flet as ft
from login_view import login_view
from register_view import register_view
from login_bibliotecario import login_bibliotecario_view
from tela_principal_bibliotecario_view import tela_principal_bibliotecario_view
from tela_principal_usuario import tela_principal_usuario_view


def main(page: ft.Page):
    page.title = "Login"

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(login_view(page))

        if page.route == "/cadastro":
            page.views.append(register_view(page))

        if page.route == "/loginadm":
            page.views.append(login_bibliotecario_view(page))

        if page.route == "/tela_principal_bibliotecario":
            page.views.append(tela_principal_bibliotecario_view(page))
        
        if page.route == "/tela_principal_usuario":
            page.views.append(tela_principal_bibliotecario_view(page))

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    ft.app(main, view=ft.AppView.WEB_BROWSER)
