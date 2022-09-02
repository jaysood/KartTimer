from PIL import Image, ImageGrab
import sys
import pytesseract

file = sys.argv[1]
print(pytesseract.image_to_string(Image.open(file)))