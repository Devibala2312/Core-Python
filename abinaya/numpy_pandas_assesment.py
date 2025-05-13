import numpy as np

import pandas as pd

# 1. Create a 1D NumPy array of the integers 5 to 10.

array_1D = np.arange(5,10)
print(array_1D)

# 2. Create a 2D numpy array with shape of (3, 3) & fill it with random numbers. Calculate the count of even numbers.

array_2d = np.random.randint(1,10, size=(3,3))
print(array_2d)
count_even_num = np.sum(array_2d % 2 == 0)
print(count_even_num)

# 3. to dataframe

data = {
    'name': ['Alice', 'Bob', 'Jefin', 'David', 'Jude'],
    'math_score': [80, 64, 90, 72, 56],
    'english_score': [78, 85, 88, 69, 60]
}

df = pd.DataFrame(data)
df.rename(columns={'name':'student_name'}, inplace=True)
df['average_score'] = ((df['math_score'] + df['english_score'])/2).astype(np.int8)

df.drop(columns=['math_score', 'english_score'], inplace=True)

print(df)

# 4. Create 2 Dataframes and concatenate them vertically & reset the index

df1 = pd.DataFrame({
    'name': ['Alice', 'Jefin', 'David'],
    'student_id': [1001, 1004, 1003]
})

df2 = pd.DataFrame({
    'name': ['Bob', 'Jude'],
    'student_id': [1002, 1005]
})

concat_vert = pd.concat([df1, df2], ignore_index=True)

print(concat_vert)

# 5. "{
# 'first_name': ['John', 'Jane', 'Alice', 'Bob'],
# 'last_name':  ['Doe',  'Smith','Johnson','Lee']
# }
# Using this data, create a data frame. Add a new column full_name by concatenating first_name and last_name with a single space between them."

name = {
 'first_name': ['John', 'Jane', 'Alice', 'Bob'],
 'last_name':  ['Doe',  'Smith','Johnson','Lee']
 }

df = pd.DataFrame(name)
df['full_name'] = df['first_name'] + ' ' + df['last_name']
print(df)

# 6. "{
# 'order_id':  [101, 102, 103, 104, 105, 106, 107],
# 'product_category':['Electronics','Clothing','Electronics', 'Home','Clothing','Home','Electronics'],
# 'order_value':  [250, 80, 120, 200, 50, 150, 300],
# 'user_id':[1, 2,  1, 3, 2, 1, 2]
# }
# 1) Calculate count of order made by each user
# 2) Average of order_value by each user.
# 3) Average order_value for each product_category"

retail_data = {
 'order_id':  [101, 102, 103, 104, 105, 106, 107],
 'product_category':['Electronics','Clothing','Electronics', 'Home','Clothing','Home','Electronics'],
 'order_value':  [250, 80, 120, 200, 50, 150, 300],
 'user_id':[1, 2,  1, 3, 2, 1, 2]
 }

retail_df = pd.DataFrame(retail_data)
print(retail_df)

count = retail_df.groupby('user_id').size().reset_index(name='order_count')
print(count)

avg_order_value = retail_df.groupby('user_id')['order_value'].median(True).reset_index(name='avg_order_value')
print(avg_order_value)

avg_prod_category = retail_df.groupby('product_category')['order_value'].mean().reset_index(name='avg_prod_category')
print(avg_prod_category)

