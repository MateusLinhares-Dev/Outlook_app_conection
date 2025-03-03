import os
import json

BASE_FILE = os.path.abspath(os.path.dirname(__file__))

def save(log: dict):
    file = os.path.join(BASE_FILE, 'register.json')

    if not os.path.exists(file):
        with open(file, 'w', encoding="utf-8") as file:
            json.dump([], file)
    
    
    with open(file, 'r', encoding='utf-8') as file_json:
        try:
            data: list[dict] = json.load(file_json)
        except json.JSONDecodeError:
            data: list = []
    
    data.append(log)

    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Salvo com sucesso!")

