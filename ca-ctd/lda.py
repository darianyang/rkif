'''
Using multiple candidate pcoords:
    * o_angle 1 / 2
    * tt_dist
    * W184 chi1 (M1/M2) - break into sin / cos contributions?
    * others? e.g. other H-bonds or the hydrophobic int distance
        * note that since labels were made using o_angles, might need something else
          to build the classifier with

Build and train linear classifier (LDA):
    * test on the 3D oa_max single pathway, target: nice linear discrimination
'''

import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

