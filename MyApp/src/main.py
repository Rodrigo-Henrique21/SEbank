import flet as ft
from frontend import Tela

def main(page: ft.Page):
    app = Tela(page)
    app.telaLogin()

ft.app(target=main, port=4040,view=ft.WEB_BROWSER)