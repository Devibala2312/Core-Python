import pandas as pd

data = pd.DataFrame({
'first_name': ['John', 'Jane', 'Alice', 'Bob'],
'last_name':  ['Doe',  'Smith','Johnson','Lee']
})
data['full_name'] = data["first_name"] + " " + data["last_name"]
print(data)