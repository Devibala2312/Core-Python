# Create a 2D numpy array with shape of (3, 3) & fill it with random numbers.
# Calculate the count of even numbers.
import numpy as np

# Eg array:[[2,3,2],[1,2,4],[5,6,7]]
# Even numbers count: 5

twod_array = np.array([[2,3,2],[1,2,4],[5,6,8]])
count = 0
for number in twod_array.flat:
    if number % 2 == 0:
        count += 1
print(f"even numbers count {count}")