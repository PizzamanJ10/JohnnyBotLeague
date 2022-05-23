# Import required packages
import pytesseract

def getText(img):
    return(pytesseract.image_to_string(img))