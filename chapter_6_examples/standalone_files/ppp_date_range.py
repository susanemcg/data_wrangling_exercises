# Quick script for finding the earliest and latest loan dates in the PPP loan
# data

# importing the `pandas` library. The `as` keyword let's us essentially create
# a nickname for the library so that we can refer to it in fewer characters
import pandas as pd

# read the recent data sample into a pandas DataFrame using the library's
# `read_csv()` method
ppp_data = pd.read_csv('public_150k_plus_recent.csv')

# in order to find the oldest and most recent dates, we need to first convert
# the values in our data set to *actual* dates. Here, we'll use the
# pandas `to_datetime()` function, and provide it with:
# 1. the column we want converted
#   (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html)
# 2. the format of the dates as they *currently* appear in our dataset
#   (https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
ppp_data['DateApproved'] = pd.to_datetime(ppp_data['DateApproved'], format='%m/%d/%Y')


# now that the values in the `DateApproved` column are actual dates, we can
# just use regular `min()` and `max()` functions to retrieve the
# oldest and most recent dates, respectively
print(ppp_data['DateApproved'].min())
print(ppp_data['DateApproved'].max())
