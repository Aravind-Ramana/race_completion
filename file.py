import pandas as pd
import numpy as np

# Load the data from the CSV file
data = pd.read_csv("processed_route_data_shayan.csv")

# Define the number of rows to group for calculating the mean
group_size = 600 
outdf = pd.DataFrame(columns=data.columns)
row_counter = 0

for i in range(0, len(data), group_size):
    batch = data[i:(i+group_size)]
    sd, cd, s, lat, long,windspeed,winddir = map(np.array, (batch[c] for c in data.columns.to_list()))

    new_step = sd.sum()
    relelevation = (sd * np.tan(np.radians(s))).sum()

    outdf.loc[row_counter] = [
        new_step, cd[-1], np.degrees(np.arctan(relelevation/new_step)), lat.mean(), long.mean(),
        windspeed.mean(), winddir.mean()
    ]
    row_counter += 1

# Save the result to a new CSV file
outdf.to_csv("processed_route_data.csv", index=False)

print("Processed data saved to 'processed_route_data.csv'")
