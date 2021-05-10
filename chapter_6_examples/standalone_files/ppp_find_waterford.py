# Quick script for finding a business within our data set by (partial) name

# importing the `pandas` library. The `as` keyword let's us essentially create
# a nickname for the library so that we can refer to it in fewer characters
import pandas as pd

# read the recent data sample into a pandas DataFrame using the library's
# `read_csv()` method
ppp_data = pd.read_csv('public_150k_plus_recent.csv')

# pandas won't let us search for a string within any column that has NA values
# so we need to create one that doesn't have any in our target column
ppp_data_named_borrowers = ppp_data[ppp_data['BorrowerName'].notna()]

# how many loans does that leave?
print(len(ppp_data_named_borrowers.index))

# as we saw from our work on the bank names, matching strings can be tricky,
# so we'll use the pandas `str.contains()` method to search for part
# of the target business name, noting that, unlike bank names,
# borrower names are in ALL CAPS.
bankruptcy_example = ppp_data_named_borrowers[ppp_data_named_borrowers['BorrowerName'].str.contains('WATERFORD RECEPTIONS')]

# transposing the result so it's easier to see what values the columns contain
print(bankruptcy_example.transpose())

no_name = ppp_data[ppp_data['LoanStatusDate'].isna()]
