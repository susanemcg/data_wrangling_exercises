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

# first, sanity-check our data
print(ppp_data[ppp_data['JobsReported'] <= 0])

# what do you know? a couple of businesses didn't report *any* jobs
# let's ditch those two for now (remember: axis 0 is rows), and the "labels"
# in this case are the ones assigned by pandas, shown all the way to the left
# in our output
ppp_data.drop(labels=[437083,765398], axis=0)

# now, calculate the dollars per job
dollars_per_job = ppp_data['CurrentApprovalAmount']/ppp_data['JobsReported']

# add the new column back into our original data set
ppp_data.insert(3, 'Dollars per Job', dollars_per_job)

# let's use the `ProcessingMethod` value to identify definitively which
# were second round loans
pps_loans = ppp_data[ppp_data['ProcessingMethod'] == 'PPS']

# select those loans that we *know* are second round and have a value of $2M
pps_got_2M = pps_loans[pps_loans['CurrentApprovalAmount'] == 2000000.00]
print("Actual $2M second-round loans:")
print(pps_got_2M.shape)

# isolate the fingerprints of businesses that got $2M second-draw loans approved
biz_names = pd.unique(pps_got_2M['BorrowerNameFingerprint'])

# convert that list to a DataFrame
biz_names_df = pd.DataFrame(biz_names, columns=['BorrowerNameFingerprint'])

# create a new array of the same length as our biz_names_df and fill with
# a flag value
fill_column = np.full((len(biz_names),1), '2Mil2ndRnd')
biz_names_df['GotSecond'] = fill_column

# now merge this new, two-column DataFrame back onto our full_data list,
# so that we (hopefully) find their first-round loans as well
second_round_max = pd.merge(ppp_data, biz_names_df, on='BorrowerNameFingerprint')

# now all the loans that share fingerprints with the ones that got the max
# amount in the second round should have the flag value '2Mil2ndRnd' in the
# 'GotSecond' column
second_max_all_loans = second_round_max[second_round_max['GotSecond'] == '2Mil2ndRnd']

# we expect this to be twice the number of businesses that received $2M
# second-round loans
print('Total # of loans approved for most orgs that got $2M for second draw:')
print(second_max_all_loans.shape)

# how much money were these businesses approved to get from the PPP, total?
total_funds = second_max_all_loans['CurrentApprovalAmount'].sum()
print("Total funds approved for identified orgs that could have second-draw max:")
print(total_funds)

# now, let's plot that new column on our selected data set

# set the seaborn theme
sns.set_theme(style="whitegrid")

# to create charts side-by-side, we'll use the matplotlib `subplots()` method
# use tuples to access the different subplots later
fig, ((row1col1)) = plt.subplots(nrows=1, ncols=1)

# plot the histogram of our date-based analysis
date_based = sns.histplot(data=second_max_all_loans, x='Dollars per Job', hue='ProcessingMethod', ax=row1col1)

plt.show()
