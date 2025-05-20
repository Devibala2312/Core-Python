# Create a 2D numpy array with shape (5,4) & fill with random numbers,
# calculate the mean(column wise) and the overall standard deviation:

# Eg array:[
#     [10,  20,  30,  40],
#     [50,  60,  70,  80],
#     [15,  25,  35,  45],
#     [55,  65,  75,  85],
#     [100, 110, 120, 130],
# ]
# Column Mean: [46., 56., 66., 76.]
# Std: 34.34

import numpy as np

twod_array = np.array([[10,  20,  30,  40],[50,  60,  70,  80],[15,  25,  35,  45],[55,  65,  75,  85],[100, 110, 120, 130]])
sumod_0 = twod_array.sum(axis=0)
print(f"Column Mean: {np.mean(twod_array,axis=0)}")
print(f"Std: {np.std(twod_array).round(2)}")