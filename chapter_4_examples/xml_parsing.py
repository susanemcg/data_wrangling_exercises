# An example of reading data from a .xml file with Python, using the "lxml" library.
# First, you'll need pip install the lxml library: https://pypi.org/project/lxml/
# A helpful tutorial can be found here: https://lxml.de/tutorial.html
# The data used here is an instance of
# https://api.stlouisfed.org/fred/series/observations?series_id=U6RATE&api_key=YOUR_API_KEY_HERE

# specify the particular "chapter" you want to import from the "lxml" library
# in this case, "etree", which stands for "ElementTree"
from lxml import etree

# we'll also import the "csv" library because we want to convert our workbook
# to a `.csv`
import csv

# in this instance, there's nothing within the data file that really identifies
# what the data is, so we'll make the filename a separate variable so that
# we can use it to both load our source data and label our output file
filename = "U6_FRED_data"

# open is a built-in function that takes two "ingredients":
# 1. a file name (the file should be in the same folder as this Python script or notebook)
# 2. a "mode": "r" for "read" or "w" for "write"
# Because the lxml library expects byte data rather than text, in this case the
# second argument "ingredient" is "rb" for "read bytes"
xml_source_file = open(filename+".xml","rb")


# pass our xml_source_file as an ingredient to the the lxml etree library's parse method
# and store the result in a variable called `xml_doc`
xml_doc = etree.parse(xml_source_file)


# there is a lot of malformed xml out there! in order to make sure that
# what looks like good xml actually *is*, we'll start by getting
# the current xml document's "root" element
document_root = xml_doc.getroot()

# let's print it out to see what it looks like. Because it's currently
# stored as byte data, we need to use the etree.tostring() method in order
# to see anything useful
print(etree.tostring(document_root))

# if the document_root is a well-formed XML element, continue with our
# wrangling efforts
if etree.iselement(document_root):


    # create our output file, naming it "xml_"+filename
    output_file = open("xml_"+filename+".csv","w")

    # there is a "writer" recipe that lets us easily write `.csv`-formatted rows
    # so, just as we did when "reading", now that we've opened our `output_file`
    # we'll use this recipe to easily write rows, instead of reading them
    output_writer = csv.writer(output_file)

    # thanks to lxml, each xml element (or "node") has a property called "attrib"
    # whose data type is a Python dictionary (dict).
    # a `dict` type has several methods of accessing its contents
    # including the `.keys()`, `.values()`, and `.items()` methods, which return
    # lists (see: https://docs.python.org/3/library/stdtypes.html#typesmapping)
    # in this case, the list returned by the `.keys()` method will be useful as column headers
    # so we'll write those to our output file first
    # in this case, all of our elements are identical, so we can just grab the
    # first one (document_root[0]) and use its keys as the column headers
    output_writer.writerow(document_root[0].attrib.keys())

    # now, we need to loop through every element in our XML file
    # in the lxml library, XML elements are already lists, so we can use a
    # simple `for...in` loop to go through it: https://lxml.de/tutorial.html#elements-are-lists
    for child in document_root:

        # now we'll use the `.values()` method to get each element's values
        # as a list, and then use that along with the
        # `writerow` recipe directly
        output_writer.writerow(child.attrib.values())

    # just for good measure, let's close the `.csv` file we just wrote all that
    # data to...
    output_file.close()
