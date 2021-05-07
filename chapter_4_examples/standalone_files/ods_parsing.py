# An example of reading data from an .ods file with Python, using the
# "pyexcel_ods" library. First, you'll need to pip install the library:
# https://pypi.org/project/pyexcel-ods/

# specify the particular "chapter" you want to import the "pyexcel_ods" library
# in this case, "get_data"
from pyexcel_ods import get_data

# we'll also import the "csv" library because we want to convert our workbook
# to a `.csv`
import csv

# because this is a very specialized library, there are fewer functions, and
# they do more in one step.  We'll start by passing  our source filename as an
# ingredient to the pyexcel_ods library's get_data "recipe"
# and store the result in a variable called `source_workbook`
source_workbook = get_data("fredgraph.ods")

# an .ods workbook can have multiple sheets
# in this case, our library converts the `.ods` data into
# Python's "OrderedDict" data type.
# Rather than having to explicitly create an iterator as we did for the `.xlsx`
# example, the `items()` method lets us access
# each sheet's name and data as a "key/value" pair
# where the entire sheet's data is stored in the "value" variable
# even though our example workbook only includes one worksheet
# we might have more in the future.
# in this case, we've descriptively called the key `sheet_name` and the value
# `sheet_data` to make clear what we're handling
for sheet_name, sheet_data in source_workbook.items():

    # let's print the value of `sheet_name` just to see what that value is
    print(sheet_name)

    # for each sheet in our workbook, we'll create a separate `.csv` file
    # to do this, we "open" a new file, but make it *writable* ("w")
    # instead of *readable* ("r"), as we have in previous examples
    # for now, we'll name it "ods_"+sheet_name
    output_file = open("ods_"+sheet_name+".csv","w")

    # there is a "writer" recipe that lets us easily write `.csv`-formatted rows
    # so, just as we did when "reading", now that we've opened our `output_file`
    # we'll use this recipe to easily write rows, instead of reading them
    output_writer = csv.writer(output_file)

    # now, we need to loop through every row in our sheet
    # `sheet_data` is already a list, so we can just loop through that list with
    # a basic `for` loop
    for row in sheet_data:

        # because each row is already a list, we can just use the
        # `writerow` recipe directly for our output file
        output_writer.writerow(row)

    # just for good measure, let's close the `.csv` file we just wrote all that
    # data to...
    output_file.close()
