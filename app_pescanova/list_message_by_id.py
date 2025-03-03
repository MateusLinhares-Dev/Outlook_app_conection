import os
import json

BASE_FILE = os.path.abspath(os.path.dirname(__file__))

def list_message_by_id(id: str):
    file = os.path.join(BASE_FILE, 'register.json')

    with open(file, 'r', encoding='utf-8') as file_json:
        try:
            data: list[dict] = json.load(file_json)
        except json.JSONDecodeError as e:
            print(e)
        
    for json_line in data:
        if json_line.get('id', None) == id:
            return json_line
    return 'Não encontrado!'