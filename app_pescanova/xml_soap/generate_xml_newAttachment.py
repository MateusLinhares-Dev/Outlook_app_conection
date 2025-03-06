import os
import base64
import xml.etree.ElementTree as ET

BASE_NAME = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
TMP_FILE_PDF = os.path.join(BASE_NAME, 'tmp')
IMG_FILE_PDF = os.path.join(BASE_NAME, 'img')

def encode_file_to_base64(file_path):
    """Lê um arquivo e o converte para base64."""
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def generate_xml_strings(workflow_id):
    """Gera um XML separado para cada arquivo e armazena em uma lista."""
    xml_list = [] 

    for folder in [TMP_FILE_PDF, IMG_FILE_PDF]:
        for file_name in os.listdir(folder):
            file_path = os.path.join(folder, file_name)
            if os.path.isfile(file_path):
                file_base64 = encode_file_to_base64(file_path)

                # Criar estrutura XML
                envelope = ET.Element("soapenv:Envelope", {
                    "xmlns:soapenv": "http://schemas.xmlsoap.org/soap/envelope/",
                    "xmlns:urn": "urn:workflow"
                })
                ET.SubElement(envelope, "soapenv:Header")
                body = ET.SubElement(envelope, "soapenv:Body")
                attachment = ET.SubElement(body, "urn:newAttachment")

                ET.SubElement(attachment, "urn:WorkflowID").text = workflow_id
                ET.SubElement(attachment, "urn:ActivityID").text = "DT-REC"
                ET.SubElement(attachment, "urn:FileName").text = file_name.strip()
                ET.SubElement(attachment, "urn:FileContent").text = file_base64

                xml_list.append(ET.tostring(envelope, encoding="utf-8", method="xml").decode())

    return xml_list


if __name__ == "__main__":
    file_name = os.listdir(TMP_FILE_PDF)[0]
    file_path = os.path.join(TMP_FILE_PDF, file_name)
    resposta = encode_file_to_base64(file_path)
    print(resposta)