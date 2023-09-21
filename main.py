import os

import flet as ft
import tunnel as tunnel
from datetime import datetime
def main(page: ft.Page):
    page.window_center()
    page.title = "Redirect Port SCF"
    page.banner

    path = os.getcwd()

    data_atual = datetime.now()
    data_especifica = datetime(2023, 12, 30)

    def btn_click(e):
        if not txt_port.value:
            txt_port.error_text = "Informe a Porta desejada.!"
            page.update()
        else:
            # agente = dropdown.value # campo para escolher agente
            port = txt_port.value
            endpoint = txt_endpoint.value
            url = tunnel.iniciar(port)
            page.clean()
            # print(tunnel.list_tunnel())
            page.add(ft.Text('Url Para acesso externo'))
            ft.Divider(),
            new_link = ft.FilledTonalButton(url=f"{url}/{endpoint}", text=f"Direcionador porta [{port}] : {url}/{endpoint}")
            page.add(new_link)
            page.add(ft.ElevatedButton("Fechar todas as conexões", on_click=btn_click_close, icon=ft.icons.CLOSE_OUTLINED,icon_color=ft.colors.ERROR))
            page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            tunnel.generate_qrcode(url, endpoint)
            page.add(ft.Image(src=f"{path}/url-qrcode.png"))
            page.update()

    def btn_click_close(e):
        tunnels = tunnel.list_tunnel()
        for tunn in tunnels:
            tunnel.stop_tunnel(tunn['public_url'])
        page.clean()
        page.add(ft.Text("Todas as conexões foram finalizadas com sucesso.."))

    txt_port = ft.TextField(label="Escolha a porta desejada.")
    dropdown = ft.Dropdown(
        label="Agente",
        hint_text="Escolha o agente.",
        options=[
            ft.dropdown.Option("2Vi7N8Xk2LTH0BU5tPDgysmLm10_86EwTxyGZd7kq8HVt5dpv", text="SRH"),
            ft.dropdown.Option("2Vi83K2j0PzozhcSGfu6l4Yzqma_7RTRY12JfMWFpAy6FQV8M", text="STM"),
            ft.dropdown.Option("2Vi8MYIwRvifQcHLejg4zUCepWz_3V1nB8qCcw6pVATDhRQQg", text="SCF"),
        ],
        autofocus=True,
    )

    txt_endpoint = ft.TextField(label="endpoint")
    if not data_atual > data_especifica:
        page.add(ft.Text("🌎 Aplicativo para criação de Tunelamento de portas local. 🚀"))
        page.add(ft.Row([txt_port, txt_endpoint, ft.ElevatedButton("Mapear", on_click=btn_click, icon=ft.icons.LINK)])),

    # page.add(ft.ElevatedButton("Fechar todas as conexões", on_click=btn_click_close, icon=ft.icons.CLOSE_OUTLINED, icon_color=ft.colors.ERROR)),

if __name__ == "__main__":
    ft.app(target=main)
    # ft.app(port= 3636, target=main, view=ft.WEB_BROWSER)


# pyinstaller --name redirect_port --onefile --icon=img.ico --noconsole main.py

# flet pack --name redirect_port --icon=img.ico main.py

