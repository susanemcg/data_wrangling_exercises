# A simple example of reading data from a .txt file with Python, using the "csv"
# library. The source data was downloaded from Jed Shugerman's research on
# prosecutor politicians:
# https://docs.google.com/spreadsheets/d/1E6Z-jZWbrKmit_4lG36oyQ658Ta6Mh25HCOBaz7YVrA/
# Discovered through Jeremy Singer-Vine's (@jsvine) "Data is Plural" newsletter:
# https://tinyletter.com/data-is-plural
# The original .tsv file was renamed with a file extension of .txt


# import the "csv" library, which will give us lots of handy code recipes
# for dealing with our data file
import csv

# open is a built-in function that takes two "ingredients":
# 1. the data file name (in the same folder as your script or notebook)
# 2. a "mode": "r" for "read" or "w" for "write"
txt_source_file = open("ShugermanProsecutorPoliticians-SupremeCourtJustices.txt","r")

# pass our tsv_source_file as an ingredient to the the csv library's DictReader
# "recipe" and store the result in a variable called `politicians_reader`
# add the "delimiter" parameter and specify the tab character, "\t"
politicians_reader = csv.DictReader(txt_source_file, delimiter='\t')

# the DictReader function has added useful information to our data,
# like a label that shows us all the values in the first or "header" row
print(politicians_reader.fieldnames)

# since even this smaller dataset is pretty large,
# let's just print the first few rows to see what's in there
for i in range(0,5):
    print (next(politicians_reader))
