import pandas as pd

# Create the data frame
data = pd.DataFrame({
    'first_name': ['John', 'Jane', 'Alice', 'Bob'],
    'last_name': ['Doe', 'Smith', 'Johnson', 'Lee']
})

# Add the full_name column
data['full_name'] = data['first_name'] + ' ' + data['last_name']

# Display the data frame
print(data)


