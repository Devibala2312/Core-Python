import pandas as pd

df = pd.DataFrame(columns=['Name', 'Age'], index=[1, 2, 3])

df.loc[1] = ['Alice', 25]
df.loc[2] = ['Bob', 30]
df.loc[3] = ['Charlie', 20]

df.sort_values(by='Age', ascending=False, inplace=True)

print(df.iloc[[0, 1]])


