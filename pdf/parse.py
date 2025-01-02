import openparse
from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image
import PyPDF2

def regular():

    pdf_path = "./pdf/docs/precalc.pdf"
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        print(text)
        
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(text)

def ocr():
    pdf_path = "./pdf/docs/pdefinal.pdf"
    images = convert_from_path(pdf_path)
    text_all = ""
    for page_num, image in enumerate(images, start=1):
        text = image_to_string(image)
        #print(f"Page {page_num} Text:\n{text}\n")
        text_all+=" "+text

    print(text_all)
def main():
    regular()


if __name__ == "__main__":
    main()
