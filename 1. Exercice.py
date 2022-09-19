import numpy as np


"""
1 1 1 1 1
1 0 0 0 1
1 0 9 0 1
1 0 0 0 1
1 1 1 1 1
This should we print out
"""

array = np.ones((5,5))
middle = np.zeros((3,3))
middle[1,1] = 9
array[1:4,1:4] = middle

print(array)
