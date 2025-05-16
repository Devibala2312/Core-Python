import numpy as np

# Create a 2D numpy array with shape (5,4) & fill with random numbers
ip_array = np.random.randint(0,10, (5,4))
print(ip_array)

# Calculate the mean(column wise) and the overall standard deviation
mean = np.mean(ip_array, axis=0)
print(mean)

std_dev = np.std(ip_array)
print(std_dev)



