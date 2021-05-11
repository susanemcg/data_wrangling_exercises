# script to merge our PPP loan data with information from the SBA's NAICS
# size requirements, found here:
# https://www.sba.gov/document/support--table-size-standards

# import pandas to facilitate the merging and sorting
import pandas as pd

# read our PPP loan data into a new dataframe
ppp_data = pd.read_csv('public_150k_plus_fingerprints.csv', dtype='string')

# read the NAICS data into a separate dataframe
sba_naics_data = pd.read_csv('SBA-NAICS-data.csv', dtype='string')

# if there's no value in the 'NAICSCode' column, replace it with the string
# "None" to avoid it getting "matched" with a random "NA" value in the
# SBA-NAICS-data.csv file
ppp_data['NAICSCode'] = ppp_data['NAICSCode'].fillna("None")

# merge the two data sets using a "left" merge, which will just "fill in" our
# PPP loan data table.
merged_data = pd.merge(ppp_sample,sba_naics_data,how='left',left_on=['NAICSCode'],right_on=['NAICS Codes'],indicator=True)

# open a file to save our merged data to
merged_data_file = open('ppp-fingerprints-and-naics.csv', 'w')

# write the merged data to an output file as a CSV
merged_data_file.write(merged_data.to_csv())

# print out the values in the '_merge' column to  see how many
# entries in our loan data don't get matched to a NAICS code in the SBA table
print(merged_data.value_counts('_merge'))

# create a new dataframe that is *just* the unmatached rows
unmatched_values = merged_data[merged_data['_merge']=='left_only']

# open a file to write the unmatched values to
unmatched_values_file = open('ppp-unmatched-naics-codes.csv', 'w')

# write a new CSV file that contains all the unmatched NAICS codes in our
# PPP loan data, along with how many times it appears
unmatched_values_file.write(unmatched_values.value_counts('NAICSCode').to_csv())
