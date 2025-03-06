import requests
import re

def instance_workflow_activity(xml: str):
    url = 'https://demoiberia.softexpert.com/apigateway/se/ws/wf_ws.php'
    headers = {
       'Content-Type':'text/xml; charset=utf-8',
       'SOAPAction': 'urn:workflow#executeActivity',
       'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3NDA3NTY1NjcsImV4cCI6MTg5ODUyMjk2NywiaWRsb2dpbiI6InVzdWFyaW9zZSJ9.GfPuLr_QfVzxN4roR2ciA4mCmHDRPaLK5EPgv3c9SvQ'
    }

    data = xml
    response = requests.post(url=url, headers=headers, data=data)
    response_text = response.text
    code = re.search(r'<Code>(.*?)</Code>', response_text)
    
    if code.group(1) == '1':
        return response_text
    return response_text