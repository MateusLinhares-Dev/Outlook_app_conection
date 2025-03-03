from . import access_token, token_expiry, get_token_outlook, time, requests
from . import generate_file
from .save_log_message import save

def get_complaint(emails: dict) -> dict:
    
    if "Reclamação" in emails.get("subject", ""):
        sender = emails.get('sender', None)
        data = {
                "subject": emails.get("subject", ""),
                "id":emails.get('id', None),
                'name_sender': sender.get('emailAddress').get('name'),
                "sender": sender.get('emailAddress').get('address')
                }
        # save dos dados da mensagem
        save(data)
        return data
    else:
        return {}

def get_attachments(message: dict):
    bytesFile = None
    global access_token

    message_id = message.get('id', None)
    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"https://graph.microsoft.com/v1.0/users/mlinhares@softexpert.com/messages/{message_id}/attachments"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response_value = response.json()

        content = response_value.get('value', None)
        
        for files in content:
            bytesFile: str = files.get('contentBytes')
            name_file: str = files.get('name')

            if name_file.endswith('.pdf'):
                generate_file.recreate_file(name_file, bytesFile)

        return

def get_messages(message_id):
    global access_token
    
    if not access_token or time.time() < token_expiry:
        access_token = get_token_outlook()
        
    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"https://graph.microsoft.com/v1.0/users/mlinhares@softexpert.com/messages/{message_id}"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter mensagem: {response.status_code}", response.text)
        return {}