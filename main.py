import flet as ft
import tunnel as tunnel
from datetime import datetime
def main(page: ft.Page):
    page.window_center()
    page.title = "Redirect Port"

    data_atual = datetime.now()
    data_especifica = datetime(2023, 6, 30)

    def btn_click(e):
        if not txt_port.value:
            txt_port.error_text = "Informe a Porta desejada.!"
            page.update()
        else:
            port = txt_port.value
            url = tunnel.iniciar(port)
            page.clean()
            page.add(ft.Text('Url Para acesso externo'))
            ft.Divider(),
            new_link = ft.FilledTonalButton(url=f"{url}", text=f"Direcionador porta [{port}] : {url}")
            page.add(new_link)
            page.add(ft.ElevatedButton("Fechar todas as conexões", on_click=btn_click_close, icon=ft.icons.CLOSE_OUTLINED,icon_color=ft.colors.ERROR))
            page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            tunnel.generate_qrcode(url)
            page.add(ft.Image(src=r"C:\Users\Equiplano\PycharmProjects\tunnel\url-qrcode.png"))
            page.update()

    def btn_click_close(e):
        tunnels = tunnel.list_tunnel()
        for tunn in tunnels:
            tunnel.stop_tunnel(tunn['public_url'])
        page.clean()
        page.add(ft.Text("Todas as conexões foram finalizadas com sucesso.."))

    txt_port = ft.TextField(label="Escolha a porta desejada.")
    if not data_atual > data_especifica:
        page.add(ft.Row([txt_port, ft.ElevatedButton("Mapear", on_click=btn_click, icon=ft.icons.LINK)])),
    # page.add(ft.ElevatedButton("Fechar todas as conexões", on_click=btn_click_close, icon=ft.icons.CLOSE_OUTLINED, icon_color=ft.colors.ERROR)),

if __name__ == "__main__":
    ft.app(target=main, port=3636)
    # ft.app(port= 3636, target=main, view=ft.WEB_BROWSER)


# pyinstaller --name redirect_port --onefile --noconsole main.py