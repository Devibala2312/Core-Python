import pandas as pd

data = pd.DataFrame({
'item':  ['apple', 'banana', 'cherry', 'dates'],
'stock': [50, 20, 0, 30],
'price': [50, 20, 100, 150]}, index=['A','B','C','D']
)
data.loc['C',["stock"]] = 10
print(data)
value = data.iloc[1,[2]].item()
print(value)
