# Quick script for determining what borrowers did (or really, did not) state
# they would use PPP loan funds for

# importing the `pandas` library. The `as` keyword let's us essentially create
# a nickname for the library so that we can refer to it in fewer characters
import pandas as pd

# read the recent data sample into a pandas DataFrame using the library's
# `read_csv()` method
ppp_data = pd.read_csv('public_150k_plus_recent.csv')

# print how many rows do not list a value for `UTILITIES_PROCEED`
print(ppp_data['UTILITIES_PROCEED'].isna().sum())

# print how many rows do not list a value for `PAYROLL_PROCEED`
print(ppp_data['PAYROLL_PROCEED'].isna().sum())

# print how many rows do not list a value for `MORTGAGE_INTEREST_PROCEED`
print(ppp_data['MORTGAGE_INTEREST_PROCEED'].isna().sum())

# print how many rows do not list a value for `RENT_PROCEED`
print(ppp_data['RENT_PROCEED'].isna().sum())

# print how many rows do not list a value for `REFINANCE_EIDL_PROCEED`
print(ppp_data['REFINANCE_EIDL_PROCEED'].isna().sum())

# print how many rows do not list a value for `HEALTH_CARE_PROCEED`
print(ppp_data['HEALTH_CARE_PROCEED'].isna().sum())

# print how many rows do not list a value for `DEBT_INTEREST_PROCEED`
print(ppp_data['DEBT_INTEREST_PROCEED'].isna().sum())

# create a new DataFrame that contains all rows reporting *only* payroll costs
# i.e. where all other costs are listed as "NA"
payroll_only = ppp_data[(ppp_data['UTILITIES_PROCEED'].isna()) & (ppp_data['MORTGAGE_INTEREST_PROCEED'].isna()) & (ppp_data['MORTGAGE_INTEREST_PROCEED'].isna()) & (ppp_data['RENT_PROCEED'].isna()) & (ppp_data['REFINANCE_EIDL_PROCEED'].isna()) &  (ppp_data['HEALTH_CARE_PROCEED'].isna()) & (ppp_data['DEBT_INTEREST_PROCEED'].isna())]

print(len(payroll_only.index))
