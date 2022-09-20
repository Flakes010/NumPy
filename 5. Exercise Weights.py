"""With your high school reunion fast approaching, you decide to get in shape and lose some weight. 
You record your weight every day for five weeks starting on a Monday.
Given these daily weights, build an array with your average weight per weekend."""

import numpy as np

dailywts = 185 - np.arange(5*7)/5

# [185.  184.8 184.6 184.4 184.2 184.  183.8 183.6 183.4 183.2 183.  182.8
#  182.6 182.4 182.2 182.  181.8 181.6 181.4 181.2 181.  180.8 180.6 180.4
#  180.2 180.  179.8 179.6 179.4 179.2 179.  178.8 178.6 178.4 178.2]

saturdays = dailywts[5:len(dailywts):7]
sundays = dailywts[6:len(dailywts):7]
weekends = np.stack([saturdays,sundays])
weekends = weekends.reshape(10)
avg_weight = weekends.sum() / len(weekends)

print(avg_weight)
