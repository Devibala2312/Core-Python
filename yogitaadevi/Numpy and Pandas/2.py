import numpy as np
data = np.random.randint(0, 10, size= (3,3))
print(data)
even_count = np.sum(data % 2 == 0)
print(even_count)