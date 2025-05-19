import pandas as pd

department = pd.DataFrame({
    'dept_id': [10, 20, 30, 40],
    'dept_name': ['HR', 'IT', 'Sales', 'Finance']
})

employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Revin', 'David', 'Devin'],
    'dept_id': [20, 10, 30, 50, 20],
    'salary': [70000, 48000, 55000, 62000, 72000]
})

merged_df = pd.merge(employees, department, on='dept_id', how='left')
merged_df = merged_df[merged_df['dept_name'].notna()]
print(merged_df[['name', 'dept_name']])

merged_df = pd.merge(employees, department, on='dept_id', how='left')
print(merged_df[['dept_name', 'name']])







