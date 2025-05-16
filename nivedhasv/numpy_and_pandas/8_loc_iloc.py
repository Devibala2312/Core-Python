import pandas as pd

# Create the data DataFrame
data = pd.DataFrame({
    'item': ['apple', 'banana', 'cherry', 'dates'],
    'stock': [50, 20, 0, 30],
    'price': [50, 20, 100, 150]
}, index=['A', 'B', 'C', 'D'])

# 1) Using loc, set the stock of cherry (index: "C") to 10 (currently 0)    
data.loc['C', 'stock'] = 10

# 2) Using iloc, retrieve the price value at row position 1, column position 2.
price_value = data.iloc[1, 2]


# Display the results
print(data)
print('price_value:', price_value)

