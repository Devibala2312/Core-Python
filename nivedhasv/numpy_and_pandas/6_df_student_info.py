import pandas as pd

# Initialize an empty DataFrame with the specified columns and indices
student_info = pd.DataFrame(columns=['Name', 'Age'], index=[1, 2, 3])

# Populate the DataFrame with the names and ages of three students
student_info.loc[1, 'Name'] = 'Alice'
student_info.loc[1, 'Age'] = 25
student_info.loc[2, 'Name'] = 'Bob'
student_info.loc[2, 'Age'] = 22
student_info.loc[3, 'Name'] = 'Charlie'
student_info.loc[3, 'Age'] = 27

# Sort the DataFrame by the 'Age' column in descending order
student_info = student_info.sort_values(by='Age', ascending=False)

# Display the names of the top two students using the .iloc method
print(student_info.iloc[:2, 0])

