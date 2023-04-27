#opencv
#pyteserract
from pdf2image import convert_from_path
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe'

import pytesseract
import cv2
img =cv2.imread("imagem.png")
string=pytesseract.image_to_string(img)
print(string)

