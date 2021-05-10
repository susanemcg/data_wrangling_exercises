# Quick script for determining how many loans have been disbursed

# importing the `pandas` library. The `as` keyword let's us essentially create
# a nickname for the library so that we can refer to it in fewer characters
import pandas as pd

# read the recent data sample into a pandas DataFrame using the library's
# `read_csv()` method
ppp_data = pd.read_csv('public_150k_plus_recent.csv')

# print a summary of values in the `LoanStatus` column
print(ppp_data['LoanStatus'].value_counts())
print(sum(ppp_data['LoanStatus'].value_counts()))
