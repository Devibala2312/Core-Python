import pandas as pd

department = pd.DataFrame({
'dept_id':   [10, 20, 30, 40],
'dept_name': ['HR', 'IT', 'Sales', 'Finance']
})
employee = pd.DataFrame({
'emp_id': [1, 2, 3, 4, 5], 
'name': ['Alice','Bob','Revin','David','Devin'], 
'dept_id': [20, 10, 30, 50, 20],
'salary': [70000, 48000, 55000, 62000, 72000]
})

# Inner Join
result = department.merge(employee)[["name","dept_name"]]
print(result)

# Left Join
result = department.merge(employee, how="left")[["name","dept_name"]]
print(result.fillna("No Department"))