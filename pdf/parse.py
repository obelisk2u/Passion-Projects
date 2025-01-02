import PyPDF2
from openai import OpenAI
import os
from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image

client = OpenAI()

def sendtogpt(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You will respond with only latex code with the answers. The answers should be numbered based on which question they correspond to. When writing LaTeX code, ensure that the expressions are properly formatted using appropriate math commands. Remove unnecessary escape sequences and redundant expressions, and ensure that each formula is clearly written in standard LaTeX syntax."},
            {"role": "user", "content": text}
        ]
    )
    message = response.choices[0].message
    print(message)
    #with open("response.txt", "w", encoding="utf-8") as file:
    #    file.write(message)


def regular():

    pdf_path = "./pdf/docs/precalc.pdf"
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        print(text)

    sendtogpt(text)   
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
