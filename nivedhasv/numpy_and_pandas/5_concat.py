# Create 2 Dataframes (with column/data of your choice) and concatenate them vertically & reset the index

import pandas as pd

# Create two DataFrames with sample data
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})


df2 = pd.DataFrame({
    'A': [7, 8, 9],
    'B': [10, 11, 12]
})


# Concatenate the DataFrames vertically
result = pd.concat([df1, df2], ignore_index=True)

# Reset the index
result.reset_index(drop=True, inplace=True)

# Display the result
print(result)







