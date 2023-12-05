"""
Generate the class assignments for major/neither/minor conformations.

For WT GDC v02:
	§ major:    <1.7Å       and     >16°
	§ neither:  1.7-3.7Å    and     9-16°
    § minor:    >3.7Å       and     <9°
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# import the rmsd and o_angle data files, only the data col not frames
rmsd = np.loadtxt("data/rmsd_bb.dat")[:,1]
oa = np.loadtxt("data/o_angle.dat")[:,1]

# array of frame labels initialized with "neither"
# structured array with a variable-length string field
# otherwise the default dtype=str only holds a single char
labels = np.zeros(len(rmsd), dtype=[("label", "U10")])

# set the default label to "neither"
labels["label"] = "neither"

# assign major and minor labels from element wise conditions
labels[(rmsd <= 1.7) & (oa >= 16)] = "major"
labels[(rmsd >= 3.7) & (oa <= 9)] = "minor"

# save the labeled class assignments structured array
#np.savetxt("WT_GDC_class_assignments.txt", labels, fmt="%s")

# make a plot of the class assignments
# Map text labels to numerical values
label_mapping = {'major': 0, 'neither': 1, 'minor': 2}  # Add more labels as needed
numerical_labels = np.array([label_mapping[label] for label in labels['label']])

# Create a colormap
colors = ['#DEE11E', '#1EDEE1', '#E11EDE']
cmap = ListedColormap(colors)

# Scatter plot
plt.scatter(rmsd, oa, c=numerical_labels, cmap=cmap, s=3)

# Add colorbar
cbar = plt.colorbar()
cbar.set_ticks([0, 1, 2])  # Adjust ticks according to your labels
cbar.set_ticklabels(list(label_mapping.keys()))

# add state label lines
# [plt.axhline(y=i, linestyle='--', color='k') for i in [9, 16]]
# [plt.axvline(x=i, linestyle='--', color='k') for i in [1.7, 3.7]]
plt.axhline(y=9, xmax=3.7, linestyle='--', color='k')

# formatting
plt.xlabel("Backbone RMSD ($\AA$)")
plt.ylabel("Orientation Angle (°)")
plt.title("WT $\gamma$D-Crystallin State Labels")

plt.show()