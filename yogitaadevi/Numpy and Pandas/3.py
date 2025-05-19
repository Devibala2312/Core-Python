import numpy as np
data = np.random.randint(0,100, size=(5,4))
print(data)
print(np.mean(data, axis=0))
print(np.std(data))