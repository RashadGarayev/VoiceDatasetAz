import pandas as pd

# Replace 'train.csv' and 'train1.csv' with your actual file paths
file_path_train = 'train.csv'
file_path_train_ = 'merge.csv'
# Load the CSV files into pandas DataFrames
df_train = pd.read_csv(file_path_train)
df_train1 = pd.read_csv(file_path_train_)
# Concatenate the two DataFrames vertically (row-wise)
merged_df = pd.concat([df_train, df_train_], ignore_index=True)
# Save the merged DataFrame to a new CSV file
merged_df.to_csv('merged.csv', index=False)
