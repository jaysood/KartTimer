from PIL import Image, ImageGrab
import sys
import pytesseract

file = "latest.jpg"

content = pytesseract.image_to_string(Image.open(file).convert('L'))
print(content)