import pandas as pd

# Load the data from the CSV file
data = pd.read_csv("raw_route_data.csv")

# Define the number of rows to group for calculating the mean
group_size = 600

# Calculate the mean for every group of 570 rows
mean_data = data.groupby(data.index // group_size).mean()
mean_data["StepDistance(m)"]*=600

# Save the result to a new CSV file
mean_data.to_csv("processed_route_data.csv", index=False)

print("Processed data saved to 'processed_route_data.csv'")
