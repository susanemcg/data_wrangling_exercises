# A basic example of reading data from a .pdf file with Python,
# using pdf2image to convert it to images, and then using the
# openCV and tesseract libraries to extract the text
# The source data was downloaded from:
# https://files.stlouisfed.org/files/htdocs/publications/page1-econ/2020/12/01/unemployment-insurance-a-tried-and-true-safety-net_SE.pdf

# the built-in `operating system` or `os` Python library will let us create
# a new folder in which to store our converted images and output text
import os

# we'll import the `convert_from_path` "chapter" of the `pdf2image` library
from pdf2image import convert_from_path

# the built-in `glob`library offers a handy way to loop through all the files
# of a certain type in a folder, without needing to specify their individual
# file names
import glob
# `cv2` is the actual library name for `openCV`
import cv2

# and of course, we need our Python library for interfacing with the tesseract
# OCR process
import pytesseract

# we'll use the pdf name to name our generated images and text files, too
pdf_name = "SafetyNet"

# our source pdf is just in the same folder as our Python script
pdf_source_file = pdf_name+".pdf"

# if a folder with the same name as the pdf does not already exist
if os.path.isdir(pdf_name) == False:
    # create a new folder with that name
    target_folder = os.mkdir(pdf_name)


# store all the pages of the PDF in a variable, by providing the path to then
# source file and the desired dots per inch (DPI) resolution of the output images
# while a lower DPI will be much faster, the poorer quality images my yield
# significantly less accurate OCR results. 300 DPI is a standard "print" quality
pages = convert_from_path(pdf_source_file, 300)


# loop through all the converted pages, enumerating them so that the page
# number can be used to label the resulting images
for page_num, page in enumerate(pages):

    # use the `.join` function to save the new files into the target_folder
    # we created above
    # we have to use the `str()` function to make the page number into a string
    # for use in the filename
    filename = os.path.join(pdf_name,"p"+str(page_num)+".png")

    # save the image of the page in system
    page.save(filename, 'PNG')

# next, go through the images in the folder and extract the text from each one
# note that '*.png' means "any file ending in .png"
# the `glob()` function creates a list of all the filenames in the specified
# folder, which in this case is the same as `pdf_name` - the folder where our
# images are stored
for img_file in glob.glob(os.path.join(pdf_name, '*.png')):

    # we need the image's file name, but `img_file` starts with the folder
    # name (e.g. "SafteyNet/" and ends in `.png`. So we'll replace the
    # forward slash with a period
    temp_name = img_file.replace("/",".")

    # `temp_name` is now something like, "SafteyNet.p1.png"
    # if we `split()` that on the period, we'll get a list like:
    # ["SafetyNet","p1","png"]
    # we want the second item, but since lists start counting at 0, we need to
    # target the item at position 1
    text_filename = temp_name.split(".")[1]

    # now! create a new, writable file, also in our target folder, that
    # has the same name as the image, but is a `.txt` file
    output_file = open(os.path.join(pdf_name,text_filename+".txt"), "w")

    # use the `cv2` library to interpret our image
    img = cv2.imread(img_file)

    # create a new variable to hold the results of using pytesseract's
    # `image_to_string()` function, which will do just that
    converted_text = pytesseract.image_to_string(img)

    # write our extracted text to our output file
    output_file.write(converted_text)

    # close the output file
    output_file.close()
