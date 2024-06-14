# print(13197.351022478437+12415.866849804792+11938.438883540466+16593.25126685112 +11865.679413820491+10870.552655633557+10145.995783995659+14883.272281976002+11248.927485141556+12670.989477832467)
import pandas as pd
import numpy as np

# File paths
input_file = 'raw_route_data.csv'
output_file = 'slope.csv'

# Read the input CSV file
df = pd.read_csv(input_file)

# Initialize lists for elevations and slopes
elevations = []
slopes = []
cumulative_distances = []

# Loop through the data in chunks of 600 points
for i in range(0, len(df), 600):
    chunk = df.iloc[i:i+600]
    if len(chunk) == 600:  # Ensure we have a full chunk of 600 points
        # Calculate elevation for each point in the chunk
        elevation = np.sum(np.tan(np.radians(chunk['Slope (deg)'])) * chunk['StepDistance(m)'])
        elevations.append(elevation)
        
        # Calculate cumulative distance for the chunk
        cumulative_distance = chunk['CumulativeDistance(km)'].iloc[-1] - chunk['CumulativeDistance(km)'].iloc[0]
        # Calculate cumulative distance for the chunk
       
        cumulative_distances.append(cumulative_distance)
        # Calculate slope
        slope = elevation / (cumulative_distance * 1000)  # Convert km to meters
        slopes.append(slope)

# Create a DataFrame with the results
results_df = pd.DataFrame({'CumulativeDistance(km)': np.cumsum(cumulative_distances),
    'Elevation': np.cumsum(elevations),
    'Slope': slopes
    
})

# Save to a new CSV file
results_df.to_csv(output_file, index=False)

print(f"Slope data saved to {output_file}")
