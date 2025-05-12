import numpy as np

result = np.random.randint(0,50,size=(3,3))
filter_array = result % 2 == 0
print(result)
even_count = len(result[filter_array])
print("Count of even numbers:", even_count)