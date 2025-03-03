from . import extraction_image
import base64
import os
import sys

BASE_NAME = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
TMP_FILE_PDF = os.path.join(BASE_NAME, 'tmp')

def recreate_file(name_file: str, bytes_file: str)-> None:
    pdf_bytes = base64.b64decode(bytes_file)

    # Abre (ou cria) o arquivo PDF para escrita binária
    path_pdf = os.path.join(TMP_FILE_PDF, name_file)
    with open(path_pdf, 'wb') as file:
        file.write(pdf_bytes)
    
    extraction_image.extration_imagem_by_pdf(path_pdf)
    