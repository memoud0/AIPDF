import PyPDF2
from PyPDF2 import PdfReader
import os

file = open("static/files/NYA.pdf", "rb")
reader = PdfReader(file)

info = reader.metadata

# print(info.title)

# print(len(reader.pages))

# print(reader.pages[0].extract_text())

def get_pdf_metadata(pdf_path):
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            reader = PdfReader(f)
            info = reader.metadata
        return info
    else:
        print(f"Error File '{pdf_path}' not found.")
        return None


def extract_text_pdf(pdf_path):
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            reader = PdfReader(f)
            results = []
            for i in range(0, len(reader.pages)):
                selected_page = reader.pages[i]
                text = selected_page.extract_text()
                results.append(text)
            return ' '.join(results)
    else:
        print(f"Error File '{pdf_path}' not found.")
        return None



