import pandas as pd

data_frame_1 = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})
data_frame_2 = pd.DataFrame({
    'Name': ['Charlie', 'David'],
    'Age': [22, 28]
})

combined_data_frame = pd.concat([data_frame_1, data_frame_2], axis=0)
combined_data_frame.reset_index(drop=True, inplace=True)
print(combined_data_frame)