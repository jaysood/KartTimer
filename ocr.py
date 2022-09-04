from PIL import Image, ImageGrab
import sys
import pytesseract
import table_ocr.util
import table_ocr.extract_tables
import table_ocr.extract_cells
import table_ocr.ocr_image
import table_ocr.ocr_to_csv

file = "latest.jpg"

content = pytesseract.image_to_string(Image.open(file).convert('L'))
print(content)

kart_table = table_ocr.extract_tables.main([file])
print(kart_table)