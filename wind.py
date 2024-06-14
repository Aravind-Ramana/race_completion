import pandas as pd

# Define the file path
csv_file_path = 'wind_speed.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
df_grouped = df.groupby(df.index // 600).mean()

# Save the modified DataFrame back to a CSV file
df_grouped.to_csv(csv_file_path, index=False)

# # Modify the WindSpeed(m/s) column by dividing its values by 3.6
# df['WindSpeed(m/s)'] = df['WindSpeed(m/s)'] / 3.6

# Save the modified DataFrame back to a CSV file


print(f"The WindSpeed(m/s) values have been successfully converted and saved to {csv_file_path}")
#import pandas as pd
# import numpy as np

# # Load the data from the CSV file
# data = pd.read_csv("raw_route_data.csv")

# # Define the number of rows to group for calculating the mean
# group_size = 600 
# outdf = pd.DataFrame(columns=data.columns)
# row_counter = 0