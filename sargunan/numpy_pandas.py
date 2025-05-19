import numpy as np
import pandas as pd

# 1 - Create a 1D NumPy array of the integers 5 to 10.

arr = np.arange(5, 11)
print(arr)

# 2 - Create a 2D numpy array with shape of (3, 3) & fill it with random numbers.
# Calculate the count of even numbers.

arr = np.random.randint(1, 20, size=(3, 3))
print("Array:\n", arr)
even_count = np.sum(arr % 2 == 0)
print("Number of even elements:", even_count)


# 3 - Create a 2D numpy array with shape (5,4) & fill with random numbers,
# calculate the mean(column wise) and the overall standard deviation:

arr = np.random.randint(1, 20, size=(5, 4))
print("Array:", arr)

mean_column_wise = np.mean(arr, axis=0)
print("Column-wise Mean:", mean_column_wise)

overall_std = np.std(arr)
print("Overall Standard Deviation:", overall_std)

# 4 - Create a DataFrame with this data, rename ""name"" column to ""student_name"" and
# add a new column named ""average"" with dtype of int8 by calculating average of 2 subjects for each student.
# After calculating average, delete ""math_score"" & ""english_score"" columns."

# data
data = {
    'name': ['Alice', 'Bob', 'Jefin', 'David', 'Jude'],
    'math_score': [80, 64, 90, 72, 56],
    'english_score': [78, 85, 88, 69, 60]
}

# Create DataFrame
df = pd.DataFrame(data)
df.rename(columns={'name': 'student_name'}, inplace=True)
df['average'] = ((df['math_score'] + df['english_score']) / 2).astype(np.int8)
df.drop(columns=['math_score', 'english_score'], inplace=True)

print(df)

# 5 - Create 2 Dataframes (with column/data of your choice) and concatenate them vertically & reset the index

df1 = pd.DataFrame({
    'ID': [1, 2],
    'Name': ['Alice', 'Bob']
})

df2 = pd.DataFrame({
    'ID': [3, 4],
    'Name': ['Charlie', 'David']
})

concatenatedf = pd.concat([df1, df2], axis=0)
concatenatedf.reset_index(drop=True, inplace=True)

print(concatenatedf)

#  6 - Initialize a DataFrame (Empty) named 'Student Info' with columns 'Name' and 'Age' and set the indices to 1, 2, and 3.
#  Populate the DataFrame with the names and ages of three students using the .loc method.
#  Then, sort the DataFrame by the 'Age' column in descending order and display the names of the top two students using the .iloc method.


df = pd.DataFrame(columns=['Name', 'Age'], index=[1, 2, 3])
df.index.name = 'Index'

df.loc[1] = ['Alice', 20]
df.loc[2] = ['Bob', 22]
df.loc[3] = ['Charlie', 19]

df_sorted = df.sort_values(by='Age', ascending=False)

names = df_sorted.iloc[:2]['Name']
print(names)

# 7 - 1. Using merge, list the name of the employee along with dept_name. Skip all the employees whose dept data not available.
# 2. Using merge, list the department names along with employee names. Ensure that all employees are included,
# even if their department data is not available.

department = {
    'dept_id':   [10, 20, 30, 40],
    'dept_name': ['HR', 'IT', 'Sales', 'Finance']
}

# Employee Data
employees = {
    'emp_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Revin', 'David', 'Devin'],
    'dept_id': [20, 10, 30, 50, 20],
    'salary': [70000, 48000, 55000, 62000, 72000]
}

df_dept = pd.DataFrame(department)
df_emp = pd.DataFrame(employees)

inner = pd.merge(df_emp, df_dept, on='dept_id', how='inner')
print("\nEmployees with valid department info: ")
print(inner[['name', 'dept_name']])

left = pd.merge(df_emp, df_dept, on='dept_id', how='left')
print("\nAll employees with department names if available: ")
print(left[['name', 'dept_name']])

# 8 - 1. Using loc, set the stock of cherry (index: "C") to 10 (currently 0)
# 2. Using iloc, retrieve the price value at row position 1, column position 2.

data = {
    'item':  ['apple', 'banana', 'cherry', 'dates'],
    'stock': [50, 20, 0, 30],
    'price': [50, 20, 100, 150]
}
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])

df.loc['C', 'stock'] = 10

price_value = df.iloc[1, 2]

print("Updated DataFrame:")
print(df)
print("\nRetrieved price at row 1, column 2:", price_value)

# 9 - create a data frame. Add a new column full_name by concatenating first_name and last_name with a single space between them

data = {
    'first_name': ['John', 'Jane', 'Alice', 'Bob'],
    'last_name':  ['Doe',  'Smith','Johnson','Lee']
}

df = pd.DataFrame(data)
df['full_name'] = df['first_name'] + ' ' + df['last_name']
print(df)

# 10 - 1. Calculate count of order made by each user
# 2. Average of order_value by each user.
# 3. Average order_value for each product_category

# Given data
data = {
    'order_id':  [101, 102, 103, 104, 105, 106, 107],
    'product_category': ['Electronics','Clothing','Electronics', 'Home','Clothing','Home','Electronics'],
    'order_value':  [250, 80, 120, 200, 50, 150, 300],
    'user_id': [1, 2, 1, 3, 2, 1, 2]
}

df = pd.DataFrame(data)

order_count = df['user_id'].value_counts().sort_index()
print("1. Order count by user_id:\n", order_count, "\n")

avg_order_by_user = df.groupby('user_id')['order_value'].mean()
print("2. Average order_value by user_id:\n", avg_order_by_user, "\n")

avg_order_by_category = df.groupby('product_category')['order_value'].mean()
print("3. Average order_value by product_category:\n", avg_order_by_category)
