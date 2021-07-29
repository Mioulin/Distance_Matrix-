import numpy as np
from distance_FC import *
m1 = np.array([[17, 0, 28], [28, 0, 6], [15, 3, 8]])
m2 = np.array([[7, 0, 9], [5, 8, 6], [7, 3, 9]])
d = distance_FC(m1, m2)
print(d.pearson())
print(d.geodesic())