import pandas as pd

data = pd.DataFrame({
'order_id':  [101, 102, 103, 104, 105, 106, 107], 
'product_category':['Electronics','Clothing','Electronics', 'Home','Clothing','Home','Electronics'], 
'order_value':  [250, 80, 120, 200, 50, 150, 300], 
'user_id':[1, 2,  1, 3, 2, 1, 2]
})

count_by_user = data.groupby("user_id")["order_id"].count()
print(count_by_user)
average_value_by_user = data.groupby("user_id")["order_value"].mean().astype('int16')
print(average_value_by_user)
average_value_by_category = data.groupby("product_category")["order_value"].mean().astype('int16')
print(average_value_by_category)
