from PIL import Image, ImageGrab
import sys
import pytesseract
import table_ocr.util
import table_ocr.extract_tables
import table_ocr.extract_cells
import table_ocr.ocr_image
import table_ocr.ocr_to_csv

kart_image = "latest.jpg"

#content = pytesseract.image_to_string(Image.open(file).convert('L'))

# def convert(image):
#     kart_table = table_ocr.extract_tables.main([image])
#     for image, tables in kart_table:
#         for table in tables:
#             cells = table.ocr.extract_cells.main(table)
#             ocr = [
#                 table_ocr.ocr_image.main(cell, None)
#                 for cell in cells
#             ]
#             for c, o in zip(cells[:3], ocr[:3]):
#                         with open(o) as ocr_file:
#                             # Tesseract puts line feeds at end of text.
#                             # Stript it out.
#                             text = ocr_file.read().strip()
#                             print("{}: {}".format(c, text))
#             return table_ocr.ocr_to_csv.text_files_to_csv(ocr)

# csv_output = convert(image)
# print(csv_output)

def main(url):
    image_tables = table_ocr.extract_tables.main([kart_image])
    print("Running `{}`".format(f"extract_tables.main([{kart_image}])."))
    print("Extracted the following tables from the image:")
    print(image_tables)
    for image, tables in image_tables:
        print(f"Processing tables for {image}.")
        for table in tables:
            print(f"Processing table {table}.")
            cells = table_ocr.extract_cells.main(table)
            ocr = [
                table_ocr.ocr_image.main(cell, None)
                for cell in cells
            ]
            print("Extracted {} cells from {}".format(len(ocr), table))
            print("Cells:")
            for c, o in zip(cells[:3], ocr[:3]):
                with open(o) as ocr_file:
                    # Tesseract puts line feeds at end of text.
                    # Stript it out.
                    text = ocr_file.read().strip()
                    print("{}: {}".format(c, text))
            # If we have more than 3 cells (likely), print an ellipses
            # to show that we are truncating output for the demo.
            if len(cells) > 3:
                print("...")
            return table_ocr.ocr_to_csv.text_files_to_csv(ocr)

if __name__ == "__main__":
    csv_output = main(kart_image)
    print()
    print("Here is the entire CSV output:")
    print()
    print(csv_output)
