import numpy as np

array = np.random.randint(1, 10, (3, 3))
print(array)

even_count = np.sum(array % 2 == 0)
print(even_count)




