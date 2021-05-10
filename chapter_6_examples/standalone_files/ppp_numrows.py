# Quick script to print out the number of rows in each of our PPP loan data files
# This is a pretty basic task, so no need to import extra libraries!

# open the August PPP data in "read" mode
august_data = open("public_150k_plus_080820.csv","r")

# the `readlines()` method can be used on any text file where each there's a
# newline at the end of each row. It puts the lines into a list, whose length
# can then be measured with the built-in `len()` method. Finally, we have to
# cast that as a string with the built-in `str()` method, or Python will yell
# us for trying to combine a string and a number.
print("August file has "+str(len(august_data.readlines()))+" rows.")

# ditto for the recent PPP data
recent_data = open("public_150k_plus_recent.csv","r")

# once again, print the number of lines
print("Recent file has "+str(len(recent_data.readlines()))+" rows.")
