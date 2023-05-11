from pyngrok import ngrok
import requests
import subprocess

def set_ngrok_auth_token(token = '21YTaWNEb99ey9jMhzHpd_5pdd1qgPoJNcTNryx1SpJ'):
    command = f"ngrok authtoken {token}"
    subprocess.run(command, shell=True)

def start_tunnel(port=2424):
    # Definindo a porta que será exposta

    # Iniciando o processo do ngrok
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
