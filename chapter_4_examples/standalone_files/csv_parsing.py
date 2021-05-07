# A simple example of reading data from a .csv file with Python
# using the "csv" library.
# The source data was sampled from the Citi Bike system data:
# https://drive.google.com/file/d/17b461NhSjf_akFWvjgNXQfqgh9iFxCu_/view?usp=sharing
# Which can be found here:
# https://s3.amazonaws.com/tripdata/index.html

# import the "csv" library, which will give us lots of handy code recipes
# for dealing with our data file
import csv

# open is a built-in function that takes two "ingredients":
# 1. the data file name (in the same folder as your script or notebook)
# 2. a "mode": "r" for "read" or "w" for "write"
csv_source_file = open("202009CitibikeTripdataExample.csv","r")

# pass our csv_source_file as an ingredient to the the csv library's DictReader
# "recipe" and store the result in a variable called `citibike_reader`
citibike_reader = csv.DictReader(csv_source_file)

# the DictReader function has added useful information to our data,
# like a label that shows us all the values in the first or "header" row
print(citibike_reader.fieldnames)

# since even this smaller dataset is pretty large,
# let's just print the first few rows to see what's in there
for i in range(0,5):
    print (next(citibike_reader))
