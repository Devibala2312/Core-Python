import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Jefin', 'David', 'Jude'],
    'math_score': [80, 64, 90, 72, 56],
    'english_score': [78, 85, 88, 69, 60]
}

df = pd.DataFrame(data)
df.rename(columns={'name': 'student_name'}, inplace=True)

df['average'] = (df['math_score'] + df['english_score']) / 2

df.drop(columns=['math_score', 'english_score'], inplace=True)

print(df)



