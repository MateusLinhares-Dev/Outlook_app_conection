import requests
import re

def extract_idp_text(xml_base: str):
    content_search = re.search(r'<urn:FileContent>(.*?)</urn:FileContent>', xml_base)
    content_base64 = content_search.group(1)
    url = r"https://w097iu1q4g.execute-api.us-east-1.amazonaws.com/default/PescaNueva"

    structed_json_base64 = {
        'arquivo_base64':content_base64
        }
        
    response = requests.post(url=url, json=structed_json_base64)

    return response.json()