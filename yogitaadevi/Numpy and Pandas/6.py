import pandas as pd
df = pd.DataFrame(columns=['Name', 'Age'], index=[1, 2, 3])
df.index.name = 'ID'
df.loc[1] = ['Alice', 20]
df.loc[2] = ['Bob', 22]
df.loc[3] = ['Charlie', 19]
df.sort_values(by='Age', ascending=False, inplace=True)
print(df.iloc[:2]['Name'])