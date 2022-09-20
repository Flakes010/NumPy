"""You ditch your job as a trial lawyer to become a gold miner.
You decide to prospect five locations underneath a 7x7 grid of land. 
How much gold do you uncover at each location?"""

import numpy as np

np.random.seed(5555)
gold = np.random.randint(low=0, high=10, size=(7,7))

# Gold Output
# [[2 3 0 5 2 0 3]
#  [8 8 0 7 1 5 3]
#  [0 1 6 2 1 4 5]
#  [4 0 8 9 9 8 7]
#  [4 2 7 0 7 2 1]
#  [9 8 9 2 5 0 8]
#  [1 9 8 2 6 4 3]]

locs = np.array([
    [0,4],
    [2,2],
    [2,3],
    [5,1],
    [6,3]
])




#Solution
first_column = locs[[0,1,2,3,4],[0]]
second_column = locs[[0,1,2,3,4],[1]]
my_gold = gold[first_column,second_column]
print(my_gold)
