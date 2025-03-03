import datetime
import json
import os
import requests
import sys

BASE_FILE = os.path.abspath(os.path.dirname(__file__))

def consultant_expiration_subscription():
    expiration = (datetime.datetime.now()).isoformat() + "Z"
    subscription_json = open(os.path.join(BASE_FILE, 'id_subscription.json'))
    data = json.load(subscription_json)

    if expiration >= data.get('expiration', None):
        return True
    
    print('Não expirou o subscription, continuando...')
    return False

def reactivate_subscription(id_subscription):
    TOKEN_OUTLOOK = os.getenv('TOKEN_OUTLOOK')

    expiration = (datetime.datetime.now() + datetime.timedelta(days=3)).isoformat() + "Z"

    url = f'https://graph.microsoft.com/v1.0/subscriptions/{id_subscription}'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {TOKEN_OUTLOOK}'
    }

    json = {
        "expirationDateTime": expiration
    }

    response = requests.patch(url=url, headers=headers, json=json)

    if response.status_code == 200:
        print('Subscription renovado com sucesso!')
    else:
        raise InterruptedError('Ocorreu um erro!') 