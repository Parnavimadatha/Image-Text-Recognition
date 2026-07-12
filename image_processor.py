import cv2
import numpy as np
import pytesseract
from PIL import Image

# Change this path if Tesseract is installed elsewhere
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image):

    image = np.array(image)

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    gray = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    text = pytesseract.image_to_string(gray)

    return text