import pandas as pd

# Create the data frame
data = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105, 106, 107], 
    'product_category':['Electronics','Clothing','Electronics', 'Home','Clothing','Home','Electronics'], 
    'order_value':  [250, 80, 120, 200, 50, 150, 300], 
    'user_id':[1, 2,  1, 3, 2, 1, 2]
})

# 1) Calculate count of order made by each user 
order_count = data['user_id'].value_counts()

# 2) Average of order_value by each user.
average_order_value = data.groupby('user_id')['order_value'].mean()

# 3) Average order_value for each product_category  
average_order_value_by_category = data.groupby('product_category')['order_value'].mean()

# Display the results
print('order_count:', order_count)
print('average_order_value:', average_order_value)
print('average_order_value_by_category:', average_order_value_by_category)


