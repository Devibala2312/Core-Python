import pandas as pd

data = {
    'item': ['apple', 'banana', 'cherry', 'dates'],
    'stock': [50, 20, 0, 30],
    'price': [50, 20, 100, 150]
}

df = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])

df.loc['C', 'stock'] = 10

print(df.iloc[1, 2])




