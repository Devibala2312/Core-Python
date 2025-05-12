import pandas as pd
data = pd.DataFrame({
'name': ['Alice', 'Bob',   'Jefin', 'David', 'Jude'], 
'math_score':[80, 64, 90, 72, 56], 
'english_score': [78, 85, 88, 69, 60]
} )
data = data.rename(columns={'name': 'student_name'}).assign(average = data[['math_score', 'english_score']].mean(axis=1))
data = data.drop(columns=['math_score', 'english_score'])
data['average'] = data['average'].astype('int8')
result = data.to_dict('list')
print(result)