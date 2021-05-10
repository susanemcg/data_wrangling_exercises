# Quick script for creating new CSVs that each contain the first few rows of
# our larger data files

# importing the `pandas` library. The `as` keyword let's us essentially create
# a nickname for the library so that we can refer to it in fewer characters
import pandas as pd

# read the august data into a pandas DataFrame using the library's
# `read_csv()` method
august_ppp_data = pd.read_csv('public_150k_plus_080820.csv')

# read the recent data into a pandas DataFrame using the library's
# `read_csv()` method
recent_ppp_data = pd.read_csv('public_150k_plus_recent.csv')

# now that we have both files in memory, let's merge them
# we're going to preserve the index here because it will be the easiest way
# to keep track of what matched (and what didn't)
merged_data = pd.merge(august_ppp_data,recent_ppp_data,how='outer',left_on=['BusinessName','Lender','DateApproved'],right_on=['BorrowerName','ServicingLenderName','DateApproved'],indicator=True)

# when we use the `indicator=True` argument/ingredient, it produces a column
# called '_merge' that shows which data set that particular row matched
# as we will see from the following print statement, that value can be
# 'both', 'left_only', or 'right_only'
print(merged_data.value_counts('_merge'))

# now that we have both files in memory, let's merge them
# we're going to preserve the index here because it will be the easiest way
# to keep track of what matched (and what didn't)
merged_data_no_date = pd.merge(august_ppp_data,recent_ppp_data,how='outer',left_on=['BusinessName','Lender'],right_on=['BorrowerName','ServicingLenderName'],indicator=True)

# when we use the `indicator=True` argument/ingredient, it produces a column
# called '_merge' that shows which data set that particular row matched
# as we will see from the following print statement, that value can be
# 'both', 'left_only', or 'right_only'
print(merged_data_no_date.value_counts('_merge'))

# now that we have both files in memory, let's merge them
# we're going to preserve the index here because it will be the easiest way
# to keep track of what matched (and what didn't)
merged_data_biz_only = pd.merge(august_ppp_data,recent_ppp_data,how='outer',left_on=['BusinessName'],right_on=['BorrowerName'],indicator=True)

# when we use the `indicator=True` argument/ingredient, it produces a column
# called '_merge' that shows which data set that particular row matched
# as we will see from the following print statement, that value can be
# 'both', 'left_only', or 'right_only'
print(merged_data_biz_only.value_counts('_merge'))
