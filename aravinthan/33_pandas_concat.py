import pandas as pd

dataFrame1 = pd.DataFrame({"name":["Aravinth","Arun"], "age":[28, 34]})
dataFrame2 = pd.DataFrame({"name":["Kavin","Praveen"], "age":[34, 28]})
result = pd.concat([dataFrame1, dataFrame2], axis=0, ignore_index=True)
print(result)