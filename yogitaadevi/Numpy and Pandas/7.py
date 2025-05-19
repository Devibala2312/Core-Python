import pandas as pd

department = {
    'dept_id': [10, 20, 30, 40],
    'dept_name': ['HR', 'IT', 'Sales', 'Finance']
}
employees = {
    'emp_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Revin', 'David', 'Devin'],
    'dept_id': [20, 10, 30, 50, 20],
    'salary': [70000, 48000, 55000, 62000, 72000]
}

df_dept = pd.DataFrame(department)
df_emp = pd.DataFrame(employees)

inner_merged = pd.merge(df_emp, df_dept, on='dept_id', how='inner')
print("1. Employees with available department data:")
print(inner_merged[['name', 'dept_name']])

left_merged = pd.merge(df_emp, df_dept, on='dept_id', how='left')
print("\n2. All employees, including those with missing department data:")
print(left_merged[['name', 'dept_name']])