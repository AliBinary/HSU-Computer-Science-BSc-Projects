import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator

df = pd.read_csv("Fun_and_Learn\\UseFul\\DelayedFlights.csv")

width = 12
height = 7
dates = df['Dates'].values.tolist()

# -------------------------------------------------------------------------------------------------


# Let's only keep the columns useful to us
df = df[['Number', 'Delay']]

# Group by Month and get the mean
delay_by_month = df.groupby(['Number']).mean()['Delay'].reset_index()


# -------------------------------------------------------------------------------------------------


# Create the figure and axes objects, specify the size and the dots per inches
fig, ax = plt.subplots(figsize=(width, height), dpi=96)

# Plot bars
bar1 = ax.bar(delay_by_month['Number'], delay_by_month['Delay'], width=0.6)


# -------------------------------------------------------------------------------------------------


# Create the grid
ax.grid(which="major", axis='x', color='#DAD8D7', alpha=0.5, zorder=1)
ax.grid(which="major", axis='y', color='#DAD8D7', alpha=0.5, zorder=1)

# Reformat x-axis label and tick labels
ax.set_xlabel('', fontsize=12, labelpad=10)  # No need for an axis label
ax.xaxis.set_label_position("bottom")
ax.xaxis.set_major_formatter(lambda s, i: f'{s:,.0f}')
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.xaxis.set_tick_params(pad=2, labelbottom=True,
                         bottom=True, labelsize=12, labelrotation=0)
labels = dates
# Map integers numbers from the series to labels list
ax.set_xticks(delay_by_month['Number'], labels)

# Reformat y-axis
ax.set_ylabel('Delay (Days)', fontsize=12, labelpad=10)
ax.yaxis.set_label_position("left")
ax.yaxis.set_major_formatter(lambda s, i: f'{s:,.0f}')
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.set_tick_params(pad=2, labeltop=False,
                         labelbottom=True, bottom=False, labelsize=12)

# Add label on top of each bar
ax.bar_label(bar1, labels=[
             f'{e:,.1f}' for e in delay_by_month['Delay']], padding=3, color='black', fontsize=8)


# -------------------------------------------------------------------------------------------------


# Remove the spines
ax.spines[['top', 'left', 'bottom']].set_visible(False)

# Make the left spine thicker
ax.spines['right'].set_linewidth(1.1)

# Add in red line and rectangle on top
ax.plot([0.12, .9], [.98, .98], transform=fig.transFigure,
        clip_on=False, color='#E3120B', linewidth=.6)
ax.add_patch(plt.Rectangle((0.12, .98), 0.04, -0.02, facecolor='#E3120B',
             transform=fig.transFigure, clip_on=False, linewidth=0))

# Add in title and subtitle
ax.text(x=0.12, y=.93, s="Average Airlines Delay from the beginning of 1402 AD onwards",
        transform=fig.transFigure, ha='left', fontsize=14, weight='bold', alpha=.8)
ax.text(x=0.12, y=.90, s="Interval by day between violations of airline covenants",
        transform=fig.transFigure, ha='left', fontsize=12, alpha=.8)

# Set source text
ax.text(x=0.1, y=0.12, s="Written by: AliTitan051",
        transform=fig.transFigure, ha='left', fontsize=10, alpha=.7)

# Adjust the margins around the plot area
plt.subplots_adjust(left=None, bottom=0.2, right=None,
                    top=0.85, wspace=None, hspace=None)

# Set a white background
fig.patch.set_facecolor('white')


# -------------------------------------------------------------------------------------------------


# Colours - Choose the extreme colours of the colour map
colours = ["#2196f3", "#bbdefb"]

# Colormap - Build the colour maps
cmap = mpl.colors.LinearSegmentedColormap.from_list(
    "colour_map", colours, N=256)
# linearly normalizes data into the [0.0, 1.0] interval
norm = mpl.colors.Normalize(
    delay_by_month['Delay'].min(), delay_by_month['Delay'].max())

# Plot bars
bar1 = ax.bar(delay_by_month['Number'], delay_by_month['Delay'], color=cmap(
    norm(delay_by_month['Delay'])), width=0.6, zorder=2)


# -------------------------------------------------------------------------------------------------


# Find the average data point and split the series in 2
average = delay_by_month['Delay'].mean()
below_average = delay_by_month[delay_by_month['Delay'] < average]
above_average = delay_by_month[delay_by_month['Delay'] >= average]


# -------------------------------------------------------------------------------------------------


# Colours - Choose the extreme colours of the colour map
colors_high = ["#bbdefb", "#2196f3"]  # Extreme colours of the high scale
colors_low = ["#c81d25", "#ff5a5f"]  # Extreme colours of the low scale

# Colormap - Build the colour maps
cmap_low = mpl.colors.LinearSegmentedColormap.from_list(
    "low_map", colors_low, N=256)
cmap_high = mpl.colors.LinearSegmentedColormap.from_list(
    "high_map", colors_high, N=256)
# linearly normalizes data into the [0.0, 1.0] interval
norm_low = mpl.colors.Normalize(below_average['Delay'].min(), average)
norm_high = mpl.colors.Normalize(average, above_average['Delay'].max())

# Plot bars and average (horizontal) line
bar1 = ax.bar(below_average['Number'], below_average['Delay'], color=cmap_low(
    norm_low(below_average['Delay'])), width=0.6, label='Below Average', zorder=2)
bar2 = ax.bar(above_average['Number'], above_average['Delay'], color=cmap_high(
    norm_high(above_average['Delay'])), width=0.6, label='Above Average', zorder=2)
plt.axhline(y=average, color='grey', linewidth=3)

# Determine the y-limits of the plot
ymin, ymax = ax.get_ylim()
# Calculate a suitable y position for the text label
y_pos = average/ymax + 0.03
# Annotate the average line
ax.text(0.88, y_pos, f'Average = {average:.1f}', ha='right',
        va='center', transform=ax.transAxes, size=8, zorder=3)

# Add legend
ax.legend(loc="best", ncol=2, bbox_to_anchor=[
          1, 1.07], borderaxespad=0, frameon=False, fontsize=8)


# -------------------------------------------------------------------------------------------------


plt.show()
