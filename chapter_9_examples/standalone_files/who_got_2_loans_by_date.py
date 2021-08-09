# import pandas for data loading/transformations
import pandas as pd
# import seaborn for visualization
import seaborn as sns
# import matplotlib for visualization support
import matplotlib.pyplot as plt
# import numpy for manipulating arrays/lists
import numpy as np

# load our data
ppp_data = pd.read_csv('public_150k_plus_borrower_fingerprint_a.csv')

# we know that second-round loans were only available after January 13, 2021
# so we're going to create a new column from the date, labeling loans as
# `first_round` or `maybe_second`

# convert the `DateApproved` column to an actual datetime data type
ppp_data['DateApproved'] = pd.to_datetime(ppp_data['DateApproved'])

# the pandas `cut()` function let's us define the boundaries and labels
# of our new column based on values in the originating column
# first boundary will be 1/13/21, since we know all loans before that date
# *must* be first-round loans
second_round_start =  pd.to_datetime('2021-01-13')

# get today's date to use as the "upper" limit on possible second-round loans
todays_date = pd.to_datetime('today')

# use 1/1/2020 as the "lower" limit, since the PPP wasn't announced until spring
program_start = pd.to_datetime('2020-01-01')

# pass our boundaries and category labels to the pandas `cut()` function
loan_round = pd.cut(ppp_data.DateApproved, bins=[program_start,second_round_start, todays_date], labels=['first_round', 'maybe_second'])

# now insert the new row we created at the position we specify
ppp_data.insert(2,'Loan Round',loan_round)

# of course, it was still possible to get a first round loan after 1/13/2021 -
# as long as you hadn't gotten one before. So we need to know how many loans
# a business has been approved for in order  to draw conclusions about
# the volume of their first and second loans

# this is a basic pivot table, which will return a Series showing the number
# of times a particular 'BorrowerNameFingerprint' appears in the data set
loan_count = ppp_data.pivot_table(index=['BorrowerNameFingerprint'], aggfunc='size')

# we need to convert our Series to a DataFrame and give it a name...
loan_count_df = loan_count.to_frame('Loan Count')

# use the `describe()` method to generate summary statistics in a single step
# the key thing here is we would expect the maximum number of loans to be 2
print("Description of duplicate borrower table:")
print(loan_count_df.describe())

# Whoops! Let's look at the businesses that have more(?) than two loans?
sorted_loan_counts = loan_count_df.sort_values(by=['Loan Count'], ascending=False)
more_than_two = sorted_loan_counts[sorted_loan_counts['Loan Count'] > 2]

# print the 'unique' businesses
print("Businesses that seem to have gotten more than 2 loans:")
print(more_than_two.shape)

print("Number of businesses that appear to have gotten precisely 2 loans:")
precisely_two = sorted_loan_counts[sorted_loan_counts['Loan Count'] == 2]
print(precisely_two.shape)

# let's use the `ProcessingMethod` value to identify definitively which
# were first and which were second round loans!
# https://data.sba.gov/dataset/ppp-foia/resource/aab8e9f9-36d1-42e1-b3ba-e59c79f1d7f0
pps_loans = ppp_data[ppp_data['ProcessingMethod'] == 'PPS']

# print out the `shape` of this DataFrame to see how many businesses we have
print("Number of loans labeled as second draw:")
print(pps_loans.shape)

# how many loans in our derived data frame were approved for precisely $2M
# during the (possibly) second draw timeframe?

# first, merge our "Loan Count" DataFrame back onto our original data set,
# so we can pull all loans that have a Loan Count of 2
ppp_data_w_lc = pd.merge(ppp_data, loan_count_df, on=['BorrowerNameFingerprint'], how='left')

# now get *all* the loans that have a Loan Count of 2
matched_two_loans = ppp_data_w_lc[(ppp_data_w_lc['Loan Count'] == 2)]

# select those loans that we think are second round and have a value of $2M
# maybe_round2_2M = matched_two_loans[(matched_two_loans['CurrentApprovalAmount'] == 2000000.00) & (matched_two_loans['Loan Round'] == 'maybe_second')]
maybe_round2_2M = matched_two_loans[(matched_two_loans['CurrentApprovalAmount'] == 2000000.00) & (matched_two_loans['Loan Round'] == 'maybe_second')]
print("Derived $2M second-round loans:")
print(maybe_round2_2M.shape)

# select those loans that we *know* are second round and have a value of $2M
pps_got_2M = pps_loans[pps_loans['CurrentApprovalAmount'] == 2000000.00]
print("Actual $2M second-round loans:")
print(pps_got_2M.shape)
