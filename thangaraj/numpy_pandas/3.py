import numpy as np

array = np.random.randint(0, 10, (5, 4))
print(array)

mean = np.mean(array, axis=0)
print(mean)

std = np.std(array)
print(std)



