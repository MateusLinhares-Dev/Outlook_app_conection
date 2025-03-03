import requests
import time
import os

# Dados de configuração
client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")
tenant_id = os.environ.get("tenent_id")
scope = "https://graph.microsoft.com/.default"

access_token = None
token_expiry = 0

def get_token_outlook():
    global access_token, token_expiry

    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scope,
    }

    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get("access_token")
        expires_in = token_data.get("expires_in", 3600)
        token_expiry = time.time() + expires_in - 300 
        
        return access_token
    else:
        print(f"Erro ao obter token: {response.json()}")
        access_token = None