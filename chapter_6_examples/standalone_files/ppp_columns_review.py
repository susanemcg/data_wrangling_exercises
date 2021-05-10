# Quick script for reviewing the all the column names in the PPP data
# to see what we can infer about them from the data itself

# importing the `pandas` library. The `as` keyword let's us essentially create
# a nickname for the library so that we can refer to it in fewer characters
import pandas as pd

# read the recent data sample into a pandas DataFrame using the library's
# `read_csv()` method
ppp_data_sample = pd.read_csv('recent_sample.csv')

# for the sake of speed, the pandas `read_csv()` method converts all missing
# entries to `NaN` (Not a Number), as described here:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
# To get these values converted to a more general (and intuitive) '<NA>'
# label, we'll use the `convertdtypes()` method, as described here:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#missing-data-na-conversion
converted_data_sample = ppp_data_sample.convert_dtypes()

# now that we have more generic values for the cells with missing data,
# transpose the whole sample
transposed_ppp_data_sample = converted_data_sample.transpose()

# print out the results!
print(transposed_ppp_data_sample)
