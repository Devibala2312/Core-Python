import pandas as pd

data = {
    'first_name': ['John', 'Jane', 'Alice', 'Bob'],
    'last_name': ['Doe', 'Smith', 'Johnson', 'Lee']
}

df = pd.DataFrame(data)

df['full_name'] = df['first_name'] + ' ' + df['last_name']

print(df)


