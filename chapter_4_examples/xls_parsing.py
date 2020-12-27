# A simple example of reading data from a .xls file with Python, using the "xrld" library.



# first, pip install the xlrd library: https://pypi.org/project/xlrd/2.0.1/
# then, import the "xlrd" library
import xlrd

# we'll also import the "csv" library because we want to convert our workbook
# to a `.csv`
import csv

# because this is a very specialized library, there are fewer functions that do more in one step
# pass our source filename as an ingredient to the the xlrd library's open_workbook "recipe"
# and store the result in a variable called `source_workbook`
# notice that this structure is similar to the one we use when working with the `csv` library
source_workbook = xlrd.open_workbook("fredgraph.xls")

# an .xlsx workbook can have multiple sheets
# like the "DictReader" function, load_workbook includes useful information,
# like a list that shows us the names of all the data sheets in our workbook
print(source_workbook.sheet_names())

# even though our example workbook only includes one worksheet
# we might have more in the future. So we'll use the "enumerate" functions
# to get both an iterator *and* the sheet name. This will help us
# create one `.csv`file per worksheet
for sheet_name in source_workbook.sheet_names():
    # we'll create a variable that points to the current worksheet by
    # passing the current value of `sheet_name` to `source_workbook`
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
    # converts the rows of `source_workbook` into a list that can be *iterated*, or looped, over
    # here's where you'll find most of the data accessing documentation:
    # https://xlrd.readthedocs.io/en/latest/api.html#xlrd-sheet
    for row in current_sheet.get_rows():

        # because each row is already a list, we can just use the
        # `writerow` recipe directly for our output file
        # a note that we'll find some serious funkiness in the "dates" This
        # produces. More on that here: https://xlrd.readthedocs.io/en/latest/dates.html
        # and how to handle it here (we'll do this later):
        # https://xlrd.readthedocs.io/en/latest/api.html#module-xlrd.xldate
        output_writer.writerow(row)

    # just for good measure, let's close the `.csv` file we just wrote all that
    # data to...
    output_file.close()
