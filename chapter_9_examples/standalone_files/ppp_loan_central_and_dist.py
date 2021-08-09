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

# use pandas' built-in `median()` & `mean()` methods
median = ppp_data['CurrentApprovalAmount'].median()
mean = ppp_data['CurrentApprovalAmount'].mean()

# Q1 is the value at the position in our data set that has 25% of data readings
# to its left
Q1 = ppp_data['CurrentApprovalAmount'].quantile(0.25)

# Q3 is the value at the position in our data set that has 75% of data readings
# to its left
Q3 = ppp_data['CurrentApprovalAmount'].quantile(0.75)

# IQR is the difference between the Q3 and Q1 values
IQR = Q3-Q1

# and now we calculate our lower and upper bounds
lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)

# now we'll use seaborn to plot the histogram
approved_loan_plot = sns.histplot(data=ppp_data, x="CurrentApprovalAmount")

# use `get_ylim()` to find the current height of the chart
y_axis_range = approved_loan_plot.get_ylim()

# add the vertical lines - including the mean to see how its position
# compares to our median & quartile-based values

# mean line in gray
approved_loan_plot.vlines(mean, 0, y_axis_range[1], color='gray', ls='-')

# other lines in black (median solid, others dotted)
approved_loan_plot.vlines(median, 0, y_axis_range[1], color='black', ls='-')
approved_loan_plot.vlines(lower_bound, 0, y_axis_range[1], color='black', ls=':')
approved_loan_plot.vlines(Q1, 0, y_axis_range[1], color='black', ls=':')
approved_loan_plot.vlines(Q3, 0, y_axis_range[1], color='black', ls=':')
approved_loan_plot.vlines(upper_bound, 0, y_axis_range[1], color='black', ls=':')

# the matplotlib `show()` method will pop up an interactive view of our
# chart, allowing us to zoom, pan and otherwise explore our histogram
plt.show()


#https://stackoverflow.com/questions/64981220/how-can-i-get-the-x-axis-value-for-the-distributions-peak-y-value-in-a-seaborn-d
# https://towardsdatascience.com/7-points-to-create-better-histograms-with-seaborn-5fb542763169
