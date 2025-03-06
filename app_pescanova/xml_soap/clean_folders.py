import os

BASE_NAME = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
TMP_FILE_PDF = os.path.join(BASE_NAME, 'tmp')
IMG_FILE_PDF = os.path.join(BASE_NAME, 'img')

def clean_folders():
    """Remove todos os arquivos das pastas especificadas."""
    for folder in [IMG_FILE_PDF, TMP_FILE_PDF]:
        for file_name in os.listdir(folder):
            file_path = os.path.join(folder, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
