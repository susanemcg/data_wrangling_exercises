# Converting data in an .xls file with Python to csv + metadata file
# using the "xrld" library. First, pip install the xlrd library:
# https://pypi.org/project/xlrd/2.0.1/

# then, import the "xlrd" library
import xlrd

# import the csv library
import csv

# start by passing our source filename as an ingredient to the xlrd library's
# open_workbook "recipe" and store the result in a variable called
# `source_workbook`.
source_workbook = xlrd.open_workbook("fredgraph.xls")

# we'll probably only need one metadata file per workbook, though we could
# easily move this inside the loop and create a per-sheet metadata file
# if necessary
source_workbook_metadata = open("fredgraph_metadata.txt","w")

# even though our example workbook only includes one worksheet, the
# `open_workbook` recipe has generated a list of sheet names that we can loop
# through. In the future, we could use this to create one  `.csv`file per sheet
for sheet_name in source_workbook.sheet_names():

    # we'll create a variable that points to the current worksheet by
    # passing the current value of `sheet_name` to the `sheet_by_name` recipe
    current_sheet = source_workbook.sheet_by_name(sheet_name)

    # for each sheet in our workbook, we'll create a separate `.csv` file
    # for clarity, we'll name it "xls_"+sheet_name
    output_file = open("xls_"+sheet_name+".csv","w")

    # there is a "writer" recipe that lets us easily write `.csv`-formatted rows
    output_writer = csv.writer(output_file)

    # we'll use a boolean (True/False) "flag" variable so that we know when
    # to start writing to our "data" file instead of our "metadata" file
    is_table_data = False

    # now, we need to loop through every row in our sheet
    for row_num, row in enumerate(current_sheet.get_rows()):

        # pulling out the value in the first column of the current row
        first_entry = current_sheet.row_values(row_num)[0]

        # if we've hit the header row of our data table
        if first_entry == 'observation_date':
            # it's time to switch our "flag" value to "True"
            is_table_data = True

        # if `is_table_data` is True
        if is_table_data:

            # write this row to the data output file
            output_writer.writerow(current_sheet.row_values(row_num))

        # otherwise, this row must be metadata
        else:
            # since we'd like our metadata file to be nicely formatted, we
            # need to loop through the individual cells of each metadata row
            for item in current_sheet.row(row_num):

                    # write the value of the cell
                    source_workbook_metadata.write(item.value)

                    # separate it from the next cell with a tab
                    source_workbook_metadata.write('\t')

            # at the end of each line of metadata, add a newline
            source_workbook_metadata.write('\n')

    # just for good measure, let's close our output files
    output_file.close()
    source_workbook_metadata.close()
