# A simple example of reading data from a .png file with Python, using the openCV and tesseract libraries
# The source data was downloaded from https://files.stlouisfed.org/files/htdocs/publications/page1-econ/2020/12/01/unemployment-insurance-a-tried-and-true-safety-net_SE.pdf

# https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/
# pip install pdf2image

# on Chromebook also need poppler: https://stackoverflow.com/questions/46184239/extract-a-page-from-a-pdf-as-a-jpeg
# sudo apt install poppler-utils

# pip install opencv-python <- for cv2 import
# need to install tesseract first, then pytesseract
# apt-get install tesseract-ocr
# pip install pytesseract

import os
from pdf2image import convert_from_path
import glob
import cv2
import pytesseract

pdf_name = "SafetyNet"

# Path of the pdf
pdf_source_file = pdf_name+".pdf"

if os.path.isdir(pdf_name) == False:
    target_folder = os.mkdir(pdf_name)


# Store all the pages of the PDF in a variable
# second argument is DPI!!
pages = convert_from_path(pdf_source_file, 300)


# Iterate through all the pages stored above
for page_num, page in enumerate(pages):

    filename = os.path.join(pdf_name,"p"+str(page_num)+".png")

    # Save the image of the page in system
    page.save(filename, 'PNG')


# next, go through the images in the folder and extract the text from each one
for img_file in glob.glob(os.path.join(pdf_name, '*.png')):
    temp = img_file.replace("/",".")
    text_filename = temp.split(".")[1]

    output_file = open(os.path.join(pdf_name,text_filename+".txt"), "w")
    img = cv2.imread(img_file)
    converted_text = str(pytesseract.image_to_string(img))
    output_file.write(converted_text)
    output_file.close()
