import pandas as pd

# Create a dictionary with the data
data = {
    'name': ['Alice', 'Bob', 'Jefin', 'David', 'Jude'],
    'math_score': [80, 64, 90, 72, 56],
    'english_score': [78, 85, 88, 69, 60]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)
print(df)

# Rename the "name" column to "student_name"
df.rename(columns={'name': 'student_name'}, inplace=True)

# Calculate the average of the two subjects
df['average'] = (df['math_score'] + df['english_score']) / 2

# Delete the "math_score" and "english_score" columns
df.drop(columns=['math_score', 'english_score'], inplace=True)

# Display the DataFrame
print(df)








