# Converting data in an .xls file with Python to csv + metadata file, with
# functional date values using the "xrld" library.
# First, pip install the xlrd library:
# https://pypi.org/project/xlrd/2.0.1/

# then, import the "xlrd" library
import xlrd

# import the csv library
import csv

# needed to test if a given value is *some* type of number
from numbers import Number

# for parsing/formatting our newly interpreted Excel dates
from datetime import datetime

def main():
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
        output_file = open("xls_"+sheet_name+"_dates.csv","w")

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

                # extract the table-type data values into separate variables
                the_date_num = current_sheet.row_values(row_num)[0]
                U6_value = current_sheet.row_values(row_num)[1]

                # if the value is a number, then the current row is *not*
                # the header row, so transform the date
                if isinstance(the_date_num, Number):
                    the_date_num = format_excel_date(the_date_num, source_workbook.datemode)

                # write this new row to the data output file
                output_writer.writerow([the_date_num, U6_value])

            # otherwise, this row must be metadata
            else:
                metadata_line = create_meta_text(current_sheet, row_num)

                source_workbook_metadata.write(metadata_line)

        # just for good measure, let's close our output files
        output_file.close()
        source_workbook_metadata.close()


def format_excel_date(a_date_num, the_datemode):

    a_date_num = xlrd.xldate.xldate_as_datetime(a_date_num, the_datemode)

    # create a new list containing the_date_num (formatted to MM/DD/YYYY
    # using the `strftime()` recipe) and the value in the second column
    formatted_date = a_date_num.strftime('%m/%d/%Y')

    return(formatted_date)

def create_meta_text(the_sheet, the_row_num):

    meta_line = ""

    # since we'd like our metadata file to be nicely formatted, we
    # need to loop through the individual cells of each metadata row
    for item in the_sheet.row(the_row_num):

            # write the value of the cell, followed by a tab character
            meta_line = meta_line + item.value + '\t'

    # at the end of each line of metadata, add a newline
    meta_line = meta_line+'\n'

    return(meta_line)

if __name__ == "__main__":
    main()
