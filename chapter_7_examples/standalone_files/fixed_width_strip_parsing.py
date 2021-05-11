# An example of reading data from a fixed-width file with Python and creating
# a well-formatted CSV file.
# The source file for this example comes from the NOAA, and can be accessed here:
# https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt
# The metadata for the file can be found here:
# https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt

# we'll start by importing the "csv" library
import csv

# variable to match our output filename to the input filename
filename = "ghcnd-stations"

# we'll just open the file in read format ("r") as usual
source_file = open(filename+".txt", "r")

# the "readlines()" method converts a text file to a list of lines
stations_list = source_file.readlines()

# as usual, we'll create an output file to write to
output_file = open(filename+".csv","w")

# and we'll use the `csv` library to create a "writer" that gives us handy
# "recipe" functions for creating our new file in csv format
output_writer = csv.writer(output_file)

# since we don't have column headers within these file we have to "hard code"
# these based on the information in the `readme.txt` file
headers = ["ID","LATITUDE","LONGITUDE","ELEVATION","STATE","NAME","GSN_FLAG","HCNCRN_FLAG","WMO_ID"]

# write our headers to the output file
output_writer.writerow(headers)

# loop through each line of our file
for line in stations_list:

    # create an empty list, to which we'll append each set of characters that
    # makes up a given "column" of data
    new_row = []

    # lines of text fucntion as just lists of characters, so we can just use
    # the indices from the readme file to identify each "column"
    # to make the resulting csv more usable, we'll apply the `strip()`
    # function to each set of characters, which will eliminate excess whitespace

    # ID: positions 1-11
    new_row.append((line[0:11]).strip())

    # LATITUDE: positions 13-20
    new_row.append((line[12:20]).strip())

    # LONGITUDE: positions 22-30
    new_row.append((line[21:30]).strip())

    # ELEVATION: positions 32-37
    new_row.append((line[31:37]).strip())

    # STATE: positions 39-40
    new_row.append((line[38:40]).strip())

    # NAME: positions 42-71
    new_row.append((line[41:71]).strip())

    # GSN_FLAG: positions 73-75
    new_row.append((line[72:75]).strip())

    # HCNCRN_FLAG: positions 77-79
    new_row.append((line[76:79]).strip())

    # WMO_ID: positions 81-85
    new_row.append((line[80:85]).strip())

    # now all that's left is to use the
    # `writerow` function to write new_row to our output file
    output_writer.writerow(new_row)

# just for good measure, let's close the `.csv` file we just created
output_file.close()
