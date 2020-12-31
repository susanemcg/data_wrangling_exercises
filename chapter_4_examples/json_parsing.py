# A simple example of reading data from a .csv file with Python, using the built-in "json" library.
# The data used here is an instance of
# https://api.stlouisfed.org/fred/series/observations?series_id=U6RATE&file_type=json&api_key=YOUR_API_KEY_HERE

# import the json library
import json

# we'll also import the "csv" library because we want to write our data out as as a `.csv`
import csv

# in this instance, there's nothing within the data file that really identifies
# what the data is, so we'll make the filename a separate variable so that
# we can use it to both load our source data and label our output file
filename = "U6_FRED_data"

# open is a built-in function that takes two "ingredients":
# 1. a file name (the file should be in the same folder as this Python script or notebook)
# 2. a "mode": "r" for "read" or "w" for "write"
json_source_file = open(filename+".json","r")

# pass our json_source_file as an ingredient to the json library's "load" method
# and store the result in a variable called `json_data`
json_data = json.load(json_source_file)

# create our output file, naming it "json_"+filename
output_file = open("json_"+filename+".csv","w")

# there is a "writer" recipe that lets us easily write `.csv`-formatted rows
# so, just as we did when "reading", now that we've opened our `output_file`
# we'll use this recipe to easily write rows, instead of reading them
output_writer = csv.writer(output_file)

# because the json library interprets every object as a Python dictionary (dict).
# we can use the `.keys()`, `.values()`, and `.items()` methods to access its
# contents. In this case, however, each of these methods returns
# a `dictionary view object` (see https://docs.python.org/3/library/stdtypes.html#dict-views)
# this means that while we can use what is returned by the `.keys()` method as
# our column headers, we'll need to tell Python to convert it to a regular list first
# once again, however, all of our elements are identical, so we can just grab the
# first one (json_data["observations"][0]) and use its keys as the column headers
output_writer.writerow(list(json_data["observations"][0].keys()))

# in most cases, the simplest way to find the name (or "key") of the main JSON object
# that holds our target data is simply to look at it. While XML data will
# often be rendered readably in a web browser, however, JSON data is usually shown
# as a single line. To get a better sense of its structure, try pasting it into:
# https://jsonlint.com/ This makes it clear that our target data is a list
# whose key is "observations"

for obj in json_data["observations"]:

    # because of the way that the `json` library works, if we try to just write the
    # rows directly, we'll get the values labeled with `dict`, rather than the data values
    # themselves. So we need to make *another* loop, to go through every value in every json object
    # one at a time. We'll print both the key and the value here, though only the latter
    # will be actually written to our new file

    # we'll create an empty list where we'll put the actual values of each object
    obj_values = []

    # for every "key" (or column) in each object....
    for key, value in obj.items():

        # let's print what's in here, just to see how the code sees it
        print(key,value)

        # just add the values to our list, so we get a nice clean `.csv`
        # `append` is a method/recipe that we can use on lists to add things to the end
        obj_values.append(value)


    # notice that the code below is left-aligned with the `for key, value in obj.items()` code above
    # this means that it will only be run *after* all the keys in a given json object have been
    # gone through, with its values appended to our list
    # now we'll actually write these rows to the output file
    output_writer.writerow(obj_values)

# just for good measure, let's close the `.csv` file we just wrote all that
# data to...
output_file.close()
