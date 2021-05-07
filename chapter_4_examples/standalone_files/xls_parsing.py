# A simple example of reading data from a .xls file with Python
# using the "xrld" library. First, pip install the xlrd library:
# https://pypi.org/project/xlrd/2.0.1/

# then, import the "xlrd" library
import xlrd

# we'll also import the "csv" library because we want to convert our workbook
# to a `.csv`
import csv

# because this is a very specialized library, there are fewer functions, and
# they do more in one step.  We'll start by passing  our source filename as an
# ingredient to the xlrd library's open_workbook "recipe" and store the result
# in a variable called `source_workbook`. Notice that this structure is similar
# to the one we use when working with the `csv` library
source_workbook = xlrd.open_workbook("fredgraph.xls")

# an .xls workbook can have multiple sheets
# like the "DictReader" function, open_workbook generates useful information,
# like a list that shows us the names of all the data sheets in our workbook
print(source_workbook.sheet_names())

# even though our example workbook only includes one worksheet, the
# `open_workbook` recipe has generated a list of sheet names that we can loop
# through. In the future, we could use this to create one  `.csv`file per sheet
for sheet_name in source_workbook.sheet_names():

    # we'll create a variable that points to the current worksheet by
    # passing the current value of `sheet_name` to the `sheet_by_name` recipe
    current_sheet = source_workbook.sheet_by_name(sheet_name)

    # let's print the value of `sheet_name` just to see what that value is
    print(sheet_name)

    # for each sheet in our workbook, we'll create a separate `.csv` file
    # to do this, we "open" a new file, but make it *writable* ("w")
    # instead of *readable* ("r"), as we have in previous examples
    # for now, we'll just name it "xlsx_"+sheet_name
    output_file = open("xls_"+sheet_name+".csv","w")

    # there is a "writer" recipe that lets us easily write `.csv`-formatted rows
    # so, just as we did when "reading", now that we've opened our `output_file`
    # we'll use this recipe to easily write rows, instead of reading them
    output_writer = csv.writer(output_file)

    # now, we need to loop through every row in our sheet
    # the function `iter_rows()` is specific to the `openpyxl` library and
    # converts the rows of `source_workbook` into a list that can be looped over.
    # Here's where you'll find most of the data accessing documentation:
    # https://xlrd.readthedocs.io/en/latest/api.html#xlrd-sheet
    for row_num, row in enumerate(current_sheet.get_rows()):

        # although each row is already a list, we want the *values* so we can
        # use the `writerow` recipe directly for our output file
        # a note that we'll find some serious funkiness in the "dates" this
        # produces. More on that here:
        # https://xlrd.readthedocs.io/en/latest/dates.html
        # And how to fix up the dates here (we'll do this later):
        # https://xlrd.readthedocs.io/en/latest/api.html#module-xlrd.xldate
        output_writer.writerow(current_sheet.row_values(row_num))

    # just for good measure, let's close the `.csv` file we just wrote all that
    # data to...
    output_file.close()
