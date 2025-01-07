from PIL import Image
from pix2tex.cli import LatexOCR
    
img = Image.open('./pdf/docs/word_problem.png')
model = LatexOCR()
print(model(img))