import os.path
import qrcode
from pyngrok import ngrok, conf, installer
import requests
import subprocess
import ssl

conf.get_default().ngrok_path = os.getcwd()+ r'\ngrok.exe'

def set_ngrok_auth_token(token = '2Vi8MYIwRvifQcHLejg4zUCepWz_3V1nB8qCcw6pVATDhRQQg'):
    command = f"ngrok authtoken {token}"
    subprocess.run(command, shell=True)
    # agente = f"ngrok config add-authtoken 2Vi7N8Xk2LTH0BU5tPDgysmLm10_86EwTxyGZd7kq8HVt5dpv"
    # subprocess.run(agente, shell=True)

def start_tunnel(port=4040):

    pyngrok_config = conf.get_default()
    if not os.path.exists(pyngrok_config.ngrok_path):
        myssl = ssl.create_default_context();
        myssl.check_hostname = False
        myssl.verify_mode = ssl.CERT_NONE
        installer.install_ngrok(pyngrok_config.ngrok_path, context=myssl)

    public_url = ngrok.connect(port, "http")

    return public_url.public_url

def stop_tunnel(public_url):
    ngrok.disconnect(public_url)

def list_tunnel():

    api_url = "http://localhost:4040/api/tunnels"
    response = requests.get(api_url)
    tunnels = response.json()["tunnels"]

    return tunnels

def iniciar(port=4040):
    set_ngrok_auth_token()
    public_url = start_tunnel(port)
    return public_url

def generate_qrcode(url, endpoint, filename='url-qrcode.png'):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(f"{url}/{endpoint}")
    qr.make(fit=True)

    img = qr.make_image(fill='green', back_color='white')
    img.save(filename)

# ngrok config upgrade # Tem que rodar depois de rodar o sistema com o token uma vez.

# Emails=
# equiplanosrh@gmail.com [2Vi7N8Xk2LTH0BU5tPDgysmLm10_86EwTxyGZd7kq8HVt5dpv]
# equiplanostm@gmail.com[2Vi83K2j0PzozhcSGfu6l4Yzqma_7RTRY12JfMWFpAy6FQV8M]
# equiplanoscf@gmail.com[2Vi8MYIwRvifQcHLejg4zUCepWz_3V1nB8qCcw6pVATDhRQQg]
# Richielly = [21YTaWNEb99ey9jMhzHpd_5pdd1qgPoJNcTNryx1SpJ]
