# A simple example of reading data from a .csv file with Python, using the "csv" library.
# The source data was sampled from the Citi Bike system data (https://www.citibikenyc.com/system-data), located here: https://s3.amazonaws.com/tripdata/index.html


# import the "csv" library, which will give us lots of handy code recipes
# for dealing with our data file
import csv

# open is a built-in function that takes two "ingredients":
# 1. a file name (the file should be in the same folder as this Python script or notebook)
# 2. a "mode": "r" for "read" or "w" for "write"
csv_source_file = open("202009CitibikeTripdataExample.csv","r")

# pass our csv_source_file as an ingredient to the the csv library's DictReader "recipe"
# and store the result in a variable called `citibike_reader`
citibike_reader = csv.DictReader(csv_source_file)

# the DictReader function has added useful information to our original data file,
# like a label that shows us all the values in the first or "header" row
print(citibike_reader.fieldnames)

# since even this smaller dataset is pretty large, let's just print the first few rows to see what's in there
for i in range(0,5):
    print (next(citibike_reader))


# BACK POCKET: below for specific range
# ITERTOOLS.SLICE to not read entire data set into memory
# for rownum, row in enumerate(citibike_reader):
#     if (rownum > 2 && rownum< 10):
#         print(row)
