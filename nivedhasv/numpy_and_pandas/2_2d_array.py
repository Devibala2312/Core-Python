import numpy as np

# Create a 2D numpy array with shape of (3, 3) & fill it with random numbers

two_d_array = np.random.randint(0, 10, (3, 3))
print(two_d_array)

# Calculate the count of even numbers
even_count = np.sum(two_d_array % 2 == 0)
print(even_count)



