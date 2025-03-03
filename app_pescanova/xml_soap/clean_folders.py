import os

def clean_folders(folders):
    """Remove todos os arquivos das pastas especificadas."""
    for folder in folders:
        for file_name in os.listdir(folder):
            file_path = os.path.join(folder, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
