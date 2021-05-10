# Quick script for creating new CSVs that each contain the first few rows of
# our larger data files

# importing the `pandas` library. The `as` keyword let's us essentially create
# a nickname for the library so that we can refer to it in fewer characters
import pandas as pd

# read the august data into a pandas DataFrame using the library's
# `read_csv()` method
august_ppp_data = pd.read_csv('public_150k_plus_080820.csv')

# the pandas `head()` function returns the column headers and first 5 rows
# of data
august_sample = august_ppp_data.head()

# write those first few rows to a CSV called `august_sample.csv`
# pandas adds an index (essentially a column with row numbers) to every
# DataFrame it creates. The second "ingredient" here specifies that we
# *don't* want those row numbers to appear in our output CSV
august_sample.to_csv('august_sample.csv', index=False)

# read the recent data into a pandas DataFrame using the library's
# `read_csv()` method
recent_ppp_data = pd.read_csv('public_150k_plus_recent.csv')

# grab the first 5 rows of data along with the column headers, using the
# `head()` function
recent_sample = recent_ppp_data.head()

# write those first few rows to a CSV called `recent_sample.csv`, making sure
# *not* to write the row index that pandas added
recent_sample.to_csv('recent_sample.csv', index=False)
