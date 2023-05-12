import os.path

from pyngrok import ngrok, conf, installer
import requests
import subprocess
import ssl

conf.get_default().ngrok_path = os.getcwd()+ r'\ngrok.exe'

def set_ngrok_auth_token(token = '21YTaWNEb99ey9jMhzHpd_5pdd1qgPoJNcTNryx1SpJ'):
    command = f"ngrok authtoken {token}"
    subprocess.run(command, shell=True)

def start_tunnel(port=2424):

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

def iniciar(port=2424):
    set_ngrok_auth_token()
    public_url = start_tunnel(port)
    return public_url
