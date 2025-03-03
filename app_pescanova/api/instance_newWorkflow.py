import requests
import re

def instance_workflow_edit_data(xml: str):
    url = 'https://demoiberia.softexpert.com/apigateway/se/ws/wf_ws.php'
    headers = {
       'Content-Type':'text/xml; charset=utf-8',
       'SOAPAction': 'urn:workflow#newWorkflowEditData',
       'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3NDA3NTY1NjcsImV4cCI6MTg5ODUyMjk2NywiaWRsb2dpbiI6InVzdWFyaW9zZSJ9.GfPuLr_QfVzxN4roR2ciA4mCmHDRPaLK5EPgv3c9SvQ'
    }

    data = xml
    response = requests.post(url=url, headers=headers, data=data)
    response_text = response.text
    code = re.search(r'<Code>(.*?)</Code>', response_text)
    
    print('code aqui: =', code.group(1))
    if code.group(1) == '1':
        record_key = re.search(r'<RecordID>(.*?)</RecordID>', response_text)

        return record_key.group(1)
    return response.text