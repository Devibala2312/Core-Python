import pandas as pd

# Create the department DataFrame
department = pd.DataFrame({
    'dept_id': [10, 20, 30, 40],
    'dept_name': ['HR', 'IT', 'Sales', 'Finance']
})

# Create the employees DataFrame
employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Revin', 'David', 'Devin'],
    'dept_id': [20, 10, 30, 50, 20],
    'salary': [70000, 48000, 55000, 62000, 72000]
})

# Merge the employees DataFrame with the department DataFrame on the 'dept_id' column
merged_df = pd.merge(employees, department, on='dept_id', how='left')

# Display the merged DataFrame
print(merged_df)

# Merge the department DataFrame with the employees DataFrame on the 'dept_id' column
merged_df = pd.merge(department, employees, on='dept_id', how='left')

# Display the merged DataFrame
print(merged_df)





