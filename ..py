import pandas as pd

# File paths
processed_data_file = 'processed_route_data.csv'
wind_speed_file = 'wind_speed.csv'

# Read processed_data.csv
processed_data_df = pd.read_csv(processed_data_file)

# Read wind_speed.csv
wind_speed_df = pd.read_csv(wind_speed_file)

# Assuming wind_speed.csv has columns 'Column1' and 'Column2' that you want to add to processed_data.csv
# Adjust column names according to your actual data
columns_to_add = ['WindSpeed(m/s)', 'Winddirection(frmnorth)']

# Concatenate or merge based on index or a common column
# Here, assuming they have the same number of rows and can be concatenated side by side
combined_df = pd.concat([processed_data_df, wind_speed_df[columns_to_add]], axis=1)

# Save the combined DataFrame back to processed_data.csv
combined_df.to_csv(processed_data_file, index=False)

print(f"The last two columns from {wind_speed_file} have been added to {processed_data_file}.")
