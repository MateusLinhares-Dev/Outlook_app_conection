from pikepdf import Pdf, PdfImage
import os

BASE_NAME = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
IMG_FILE_PDF = os.path.join(BASE_NAME, 'img')

def extration_imagem_by_pdf(pdf_path: str) -> None:
    pdf_open = Pdf.open(pdf_path)

    for page in pdf_open.pages:
        for name, image in page.images.items():
            image_save = PdfImage(image)
            image_save.extract_to(fileprefix=f'{IMG_FILE_PDF}/{name}')
            