import numpy as np


"""
This array is given:
1 2 3 [4 5]
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 [24 25]
26 27 28 [29 30]
print out the marked numbers
"""

array = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
a = array[[0,4,5],3:]
print(a)