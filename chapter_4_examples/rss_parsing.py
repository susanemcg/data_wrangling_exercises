# An example of reading data from a .xml file with Python, using the "lxml" library.
# First, you'll need pip install the lxml library: https://pypi.org/project/lxml/
# The data used here is an instance of
# http://feeds.bbci.co.uk/news/science_and_environment/rss.xml

# specify the particular "chapter" you want to import from the "lxml" library
# in this case, "etree", which stands for "ElementTree"
from lxml import etree

# we'll also import the "csv" library because we want to convert our workbook
# to a `.csv`
import csv

# even though there is content inside our RSS we could use to identify the
# output file, the easiest thing to do is just give it the same file name
# with a `.csv` extension - then we'll know what data source it goes with!
filename = "BBC News - Science & Environment XML Feed"

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

# if the document_root is a well-formed XML element, continue with our
# wrangling efforts
if etree.iselement(document_root):

    # create our output file, naming it "rss_"+filename
    output_file = open("rss_"+filename+".csv","w")

    # there is a "writer" recipe that lets us easily write `.csv`-formatted rows
    # we'll use this recipe to easily write rows, instead of reading them
    output_writer = csv.writer(output_file)


    # as always, we'll want to balance what we handle programmatically and what
    # we review visually. In looking at our data, it's clear that each article's
    # information is stored in a separate `item` element. since copying over
    # the individual tag and attribute names would be time-consuming and error-
    # prone, however, we'll go through *one* item element and make a list of
    # all the tags (and attributes) within it, which we'll then use as the column
    # headers for our output `.csv` file

    # document_root[0] is the "channel" element
    main_channel = document_root[0]

    # the `find()` method returns *only* the first instance of the element name
    article_example = main_channel.find('item')

    # create an empty list in which to store our future column headers
    tag_list = []

    # iterdescendants() is a method particular to the lxml library, which returns
    # *only* the descendants of an element. The more common iter() method would
    # return both the element *itself* and its "descendants"
    # https://lxml.de/api.html#iteration
    for child in article_example.iterdescendants():
        # child.tag will provide the text of the tagname of the element
        # for example, for the <pubDate> element it will return "pubDate"
        # add each tag to our would-be header list
        tag_list.append(child.tag)

        # only one tag in our <item> element has an attribute, but we still want
        # to include it in our output

        # if the current tag has any attributes...
        if child.attrib:

            # we want the name or "key" of the attribute
            # the .keys() method will give us a list, so even though there is
            # only one attribute, we need to write a `for...in` loop to
            # go through and get its name as a string (instead of a one-item list)
            # fortunately, this code can be easily reused where we have multiple
            # attributes
            for attribute_name in child.attrib.keys():

                # append the attribut name to our `tag_list` column headers
                tag_list.append(attribute_name)


    # that whole `article_example` for loop was just to build `tag_list`
    # now that we're done, we'll write its contents to our output file as
    # column headers
    output_writer.writerow(tag_list)


    # now we want to grab *every* <item> elment in our file
    # so we use the `findall()` method instead of 'find()', as we did above
    for item in main_channel.findall('item'):

        # empty list for holding our new row's content
        new_row = []

        # now we'll use our list of tags to get the contents of each element
        # within each item
        for tag in tag_list:

            # if there is anything in the element with a given tag name
            if item.findtext(tag):
                # append it to our new row
                new_row.append(item.findtext(tag))
            # otherwise, make sure it's the "isPermaLink" attribute
            elif tag == "isPermaLink":

                # and grab its value from the <guid> element
                # and append it to our row
                new_row.append(item.find('guid').get("isPermaLink"))

        # write the new row to our output file!
        output_writer.writerow(new_row)

    # just for good measure, let's close the `.csv` file we just wrote all that
    # data to
    output_file.close()
