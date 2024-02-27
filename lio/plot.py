import numpy as np # used only to generate the data actually
import matplotlib.pyplot as plt


# Data section: we'd get this data from somewhere usually. 
# In this case I will create some dummy data and some dummy labels.
# We define some dummy data
Y = np.arange(5)
X = [25,12,9,8,5]
sizes = [300,150,100,150,30]


y_labels = ['gene A',
            'gene B\ngene C\ngene D',
            'potato',
            'todays dinner',
            'my favourite neighbour\nand his cat']


# Plotting section (what we are interested in)

# Create the figure and the axes. The axes is what we need
fig, ax = plt.subplots(1,1, figsize=(6,3))

# Make the scatter plot
sc = ax.scatter(X, Y[::-1], s=sizes, c='tab:red', alpha=0.5)

# For some reason, plt always puts another tick in the axes.
# Here i put the correct ticks (one for each gene)
ax.set_yticks([0,1,2,3,4])

# Put the y tick labels. Since I want from top to bottom, I 
# invert the order (y_labels[::-1]) but this depends on what you want to do
ax.set_yticklabels(y_labels[::-1])

# Set the x_label
ax.set_xlabel('-log(pValue)')

# Lets use only some nice values for the x_ticsk
ax.set_xticks([5,10,15,20,25])

# Make the y-axis a bit more range so it looks nicer
ax.set_ylim(-0.5,4.5)

# Make the legend
ax.legend(*sc.legend_elements(prop='sizes',
                              num=3,
                              color='tab:red'), # this is cool, I copied it from stackoverflow
          labelspacing=1, # more distance between labels
          loc = (1.05, 0.2), # Legend position, relative to plot
          frameon=False, # Wanna draw the frame?
          title='Genes from input')

# Set the title
ax.set_title('Some chart with gene enrichments')

# Final adjustment: organize the plot position in respect to the window
fig.subplots_adjust(left=0.25, bottom=0.2, right=0.7, top=0.9)
plt.show()
