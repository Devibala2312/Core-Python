import pandas as pd

data = {
    'order_id': [101, 102, 103, 104, 105, 106, 107],
    'product_category': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Clothing', 'Home', 'Electronics'],
    'order_value': [250, 80, 120, 200, 50, 150, 300],
    'user_id': [1, 2, 1, 3, 2, 1, 2]
}

df = pd.DataFrame(data)

print("1. Order count per user:\n", df['user_id'].value_counts().sort_index())
print("\n2. Average order value per user:\n", df.groupby('user_id')['order_value'].mean())
print("\n3. Average order value per product category:\n", df.groupby('product_category')['order_value'].mean())