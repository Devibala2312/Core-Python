import numpy as np

result = np.random.randint(low=200,  size=(5,4))
np.mean(result, axis=0)
np.std(result).round(2)