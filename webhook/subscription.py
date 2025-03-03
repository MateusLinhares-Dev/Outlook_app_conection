import requests
import datetime
import json
import sys
import os
from class_tokens import TokensSubscription

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app_pescanova.app_pescanova import get_token_outlook # type: ignore

# Configurações
WEBHOOK_URL = "https://cb01-187-87-96-69.ngrok-free.app/outlook-webhook"
BASE_FILE = os.path.abspath(os.path.dirname(__file__))

def subscription_outlook():
    ACCESS_TOKEN = get_token_outlook()
    expiration = (datetime.datetime.utcnow() + datetime.timedelta(days=3)).isoformat() + "Z"

    subscription_data = {
        "changeType": "created",
        "notificationUrl": WEBHOOK_URL,
        "resource": f"/users/mlinhares@softexpert.com/mailFolders/AAMkAGZlMDJkOWJjLWFkOGMtNDIzZi05MzQyLTM2MGJlOWI3YTEyYwAuAAAAAACEuF-O3TuJRpEWPXpxuATZAQAI-gJw1JxeTosBTL96eg88AABFJzgCAAA=/messages",
        "expirationDateTime": expiration
    }

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://graph.microsoft.com/v1.0/subscriptions", headers=headers, json=subscription_data)

    
    if response.status_code == 201:
        print("✅ Subscription criada com sucesso!")
        response_subscription = response.json()
        print(json.dumps(response_subscription, indent=2))
        setattr(TokensSubscription, 'id_subscription', response_subscription.get('id', None))
        setattr(TokensSubscription, 'expiration', expiration)

        # Salva o ID do subscription -> para renovação
        file_json_subscription = os.path.join(BASE_FILE, 'id_subscription.json')
        out_file_json = open(file_json_subscription, 'w')
        token_subscription_id = TokensSubscription.id_subscription
        json.dump(
            {
                'id':token_subscription_id,
                'expiration':expiration 
             },
             out_file_json, 
            indent=2
            )
        out_file_json.close()
    else:
        print("❌ Erro ao criar subscription:", response.status_code, response.text)

if __name__ == '__main__':
    subscription_outlook()