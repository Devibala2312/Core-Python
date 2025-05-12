import pandas as pd

StudentInfo = pd.DataFrame(columns=["Name", "Age"], index=[1,2,3])
StudentInfo.loc[1] = ["Aravinth", 28]
StudentInfo.loc[2] = ["Arun", 34]
StudentInfo.loc[3] = ["Kavin", 30]
StudentInfo.sort_values(by="Age", ascending=False, inplace=True)
StudentInfo.iloc[0:2]