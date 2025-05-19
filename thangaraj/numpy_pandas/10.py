import pandas as pd

data = {
    'order_id': [101, 102, 103, 104, 105, 106, 107],
    'product_category': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Clothing', 'Home', 'Electronics'],
    'order_value': [250, 80, 120, 200, 50, 150, 300],
    'user_id': [1, 2, 1, 3, 2, 1, 2]
}

df = pd.DataFrame(data)



print(df['user_id'].value_counts())
print(df.groupby('user_id')['order_value'].mean())


