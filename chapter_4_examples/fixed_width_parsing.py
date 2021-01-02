# An example of reading data from a fixed-width file with Python.
# The source file for this example comes from the NOAA, and can be accessed here:
# https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt
# The metadata for the file can be found here:
# https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt

# we'll start by importing the "csv" library because we want to convert
# fixed-width file to a `.csv`
import csv

filename = "ghcnd-stations"

# reading from a basic text file doesn't require any special libraries
# so we'll just open the file in read format ("r") as usual
source_file = open(filename+".txt", "r")

# the built-in "readlines()" method does just what you'd think:
# it reads in a text file and converts it to a list of lines
stations_list = source_file.readlines()

# as usual, we'll create an output file to write to
output_file = open(filename+".csv","w")

# and we'll use the `csv` library to create a "writer" that gives us handy
# "recipe" functions for creating our new file in csv format
output_writer = csv.writer(output_file)

# since we don't have anything *within* the file that we can draw on for column
# headers, we will just need to "hard code" these based on the information in
# the `readme.txt` file
# note that I've eliminated special characters and used underscores in place of
# spaces. While not strictly necessary, this can minimize hassles when cleaning
# and analyzing our data later on
headers = ["ID","LATITUDE","LONGITUDE","ELEVATION","STATE","NAME","GSN_FLAG","HCNCRN_FLAG","WMO_ID"]

# write our headers to the output file
output_writer.writerow(headers)

# loop through each line of our file
for line in stations_list:

    # let's print what's on each line just to see what it is
    #print(line)

    # create an empty list, to which we'll append each set of characters that
    # makes up a given "column" of data, according to our `readme.txt` description
    new_row = []

    # Python actually views lines of text as just lists of characters, so we can
    # just tell it to give us the characters that begin at one position (or index)
    # and end before another
    # note that, like the `range()` function, the first number is included,
    # but the second number is not. Also Python starts counting lists
    # of items at zero (often called "zero-indexing"). This means that for
    # each entry, the first number will be *one less* than whatever the metadata
    # says, but the right-hand number will be the same

    # ID: positions 1-11
    new_row.append(line[0:11])

    # LATITUDE: positions 13-20
    new_row.append(line[12:20])

    # LONGITUDE: positions 22-30
    new_row.append(line[21:30])

    # ELEVATION: positions 32-37
    new_row.append(line[31:37])

    # STATE: positions 39-40
    new_row.append(line[38:40])

    # NAME: positions 42-71
    new_row.append(line[41:71])

    # GSN_FLAG: positions 73-75
    new_row.append(line[72:75])

    # HCNCRN_FLAG: positions 77-79
    new_row.append(line[76:79])

    # WMO_ID: positions 81-85
    new_row.append(line[80:85])

    # now all that's left is to use the
    # `writerow` function to write new_row to our output file
    output_writer.writerow(new_row)

# just for good measure, let's close the `.csv` file we just wrote all that
# data to...
output_file.close()
