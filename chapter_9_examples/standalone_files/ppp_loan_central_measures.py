# we'll use pandas to read in our data
import pandas as pd
# the seaborn library offers us some nice built-in themes and chart types
import seaborn as sns
# matplotlib is the foundational library for Python visualization
import matplotlib.pyplot as plt

# read in our data
ppp_data = pd.read_csv('public_150k_plus_221.csv')

# set a basic color theme for our visualization
sns.set_theme(style="whitegrid")

# the `CurrentApprovalAmount` column in our PPP data tells us the dollar amount
# of each loan that is currently approved (whether or not it has been disbursed)

# we can use pandas' built-in `mean()` and `median()` methods to caculate
# these values
mean=ppp_data['CurrentApprovalAmount'].mean()
median=ppp_data['CurrentApprovalAmount'].median()

# we provide our pandas dataframe and the name of the data column that we want
# to use to the seaborn library's `histplot` method
approved_loan_plot = sns.histplot(data=ppp_data, x="CurrentApprovalAmount")

# we then add vertical lines our histogram where the mean and the median
# are located

# to determine how tall the lines should be, we use the `get_ylim` method,
# which returns the lowest and highest y-axis value as a list
y_axis_range = approved_loan_plot.get_ylim()

# now we'll actually add the vertical lines at the correct locations,
# specifying x position, y starting point, y ending point, color and linestyle
approved_loan_plot.vlines(mean, 0, y_axis_range[1], color='crimson', ls=':')
approved_loan_plot.vlines(median, 0, y_axis_range[1], color='green', ls='-')

# the matplotlib `show()` method will pop up an interactive view of our
# chart, allowing us to zoom, pan and otherwise explore our histogram
plt.show()


#https://stackoverflow.com/questions/64981220/how-can-i-get-the-x-axis-value-for-the-distributions-peak-y-value-in-a-seaborn-d
# https://towardsdatascience.com/7-points-to-create-better-histograms-with-seaborn-5fb542763169
