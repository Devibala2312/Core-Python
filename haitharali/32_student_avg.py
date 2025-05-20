# {
# 'name': ['Alice', 'Bob',   'Jefin', 'David', 'Jude'],
# math_score':[80, 64, 90, 72, 56],
# english_score': [78, 85, 88, 69, 60]
# }
# Create a DataFrame with this data, rename "name" column to "student_name" and
# add a new column named "average" with dtype of int8 by calculating average of 2 subjects for each student.
# After calculating average, delete "math_score" & "english_score" columns.
import pandas as pd

# The output dataframe must only have 2 cols, student_name, average. The dtype of averge must be int8.
# Dict version of output: {
#     'student_name': ['Alice', 'Bob', 'Jefin', 'David', 'Jude'],
#     'average': [79, 74, 89, 70, 58]
# }
data = {'name': ['Alice', 'Bob',  'Jefin', 'David', 'Jude'],
        'math_score':[80, 64, 90, 72, 56],
        'english_score': [78, 85, 88, 69, 60] }
df = pd.DataFrame(data)
df = df.rename(columns={'name':'student_name'})
df['average'] = ((df['math_score']+df['english_score'])//2).astype('int8')
df = df.drop(['math_score', 'english_score'], axis=1)
updated_df=df.to_dict(orient='list')
print(updated_df)