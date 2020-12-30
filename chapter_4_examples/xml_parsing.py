# An example of reading data from a .xml file with Python, using the "lxml" library.
# First, you'll need pip install the lxml library: https://pypi.org/project/lxml/

# specify the particular "chapter" you want to import from the "lxml" library
# in this case, "etree", which stands for "ElementTree"
from lxml import etree

# we'll also import the "csv" library because we want to convert our workbook
# to a `.csv`
import csv

# because this is a very specialized library, there are fewer functions that do more in one step
# pass our source filename as an ingredient to the the pyexcel_ods library's get_data "recipe"
# and store the result in a variable called `source_workbook`
xml_source_file = open("U6_FRED_data.xml","rb")


xml_doc = etree.parse(xml_source_file)


document_root = xml_doc.getroot()



print(etree.iselement(document_root))

# elements are lists: https://lxml.de/tutorial.html#elements-are-lists
for child in document_root:
    # print(etree.tostring(child))
    #print(child.attrib)
    attr_as_dict = dict(child.attrib)
    for key, value in attr_as_dict.items():
        print(value)
    #for attribute in child.attrib:
        # attrib is a dict

        #print(attribute)
# for element in document_root.iter("observation"):
#     # so we can use the wildcard ("*") above, but then we'll get the root, plus each observation
#     # so we want to limit it to the observations
#     print(etree.tostring(element))
#
#     # let's print the value of `sheet_name` just to see what that value is
#     print(sheet_name)
#
#     # for each sheet in our workbook, we'll create a separate `.csv` file
#     # to do this, we "open" a new file, but make it *writable* ("w")
#     # instead of *readable* ("r"), as we have in previous examples
#     # for now, we'll name it "ods_"+sheet_name
#     output_file = open("ods_"+sheet_name+".csv","w")
#
#     # there is a "writer" recipe that lets us easily write `.csv`-formatted rows
#     # so, just as we did when "reading", now that we've opened our `output_file`
#     # we'll use this recipe to easily write rows, instead of reading them
#     output_writer = csv.writer(output_file)
#
#     # now, we need to loop through every row in our sheet
#     # `sheet_data` is already a list, so we can just loop through that list with
#     # a basic `for` loop
#     for row in sheet_data:
#
#         # because each row is already a list, we can just use the
#         # `writerow` recipe directly for our output file
#         output_writer.writerow(row)
#
#     # just for good measure, let's close the `.csv` file we just wrote all that
#     # data to...
#     output_file.close()
