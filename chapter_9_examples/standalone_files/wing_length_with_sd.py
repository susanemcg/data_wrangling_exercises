# we'll use pandas to read in our data
import pandas as pd
# the seaborn library offers us some nice built-in themes and chart types
import seaborn as sns
# matplotlib is the foundational library for Python visualization
import matplotlib.pyplot as plt
# the statistics library has built-in functions for many statistical measures
import statistics

# read in our data
wing_data = pd.read_csv('wing_length - s057.csv')

# set a basic color theme for our visualization
sns.set_theme(style="white")

# create the histogram, allowing seaborn to choose default bin values
# the `kde` parameter let's us add a smoothed line to our visualization,
# which approximates the pattern we would expect if we had infinite data points
wing_plot = sns.histplot(data=wing_data, x="wing_length (0.1mm)", kde="True")

# here we use the statistics library's `stdev` method, though we could also use
# pandas: pd_value = wing_data['wing_length (0.1mm)'].std()
sd = statistics.stdev(wing_data['wing_length (0.1mm)'])

# time to plot some lines!

# get the max y value, to assign the line height
y_axis_range = wing_plot.get_ylim()

# plot the mean as a solid line
mean=wing_data['wing_length (0.1mm)'].mean()
wing_plot.vlines(mean, 0, y_axis_range[1], color='gray', ls='-')

# plot the three standard deviation boundary lines on either side of the mean
# recall that the loop stops *before* the higher value in `range()`
# starting with a negative number means we actually subtract from the mean
# at first
for i in range(-3,4):
    # find the current boundary value
    boundary_value = mean + (i*sd)
    # don't draw a second line over the mean line
    if boundary_value != mean:
        # plot a dotted gray line at each boundary value
        wing_plot.vlines(boundary_value, 0, y_axis_range[1], color='gray', ls=':')

# show the plot!
plt.show()
