# Quick script for finding the minimum and maximum loans currently approved
# in our PPP loan data set

# importing the `pandas` library. The `as` keyword let's us essentially create
# a nickname for the library so that we can refer to it in fewer characters
import pandas as pd

# read the recent data sample into a pandas DataFrame using the library's
# `read_csv()` method
ppp_data = pd.read_csv('public_150k_plus_recent.csv')

# just use regular `min()` and `max()` functions to retrieve the
# largest and smallest values, respectively
print(ppp_data['CurrentApprovalAmount'].min())
print(ppp_data['CurrentApprovalAmount'].max())
