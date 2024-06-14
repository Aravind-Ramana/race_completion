import pandas as pd
import matplotlib.pyplot as plt

# File path
output_file = 'slope.csv'

# Read the generated CSV file
results_df = pd.read_csv(output_file)

# Plot elevation vs. cumulative distance
plt.figure(figsize=(10, 6))
plt.plot(results_df['CumulativeDistance(km)'], results_df['Elevation'], marker='o')
plt.axvline(x=322, color='g', linestyle='-.', linewidth=3)
plt.axvline(x=588, color='g', linestyle='-.', linewidth=3)
plt.axvline(x=987, color='g', linestyle='-.', linewidth=3)
plt.axvline(x=1210, color='g', linestyle='-.', linewidth=3)
plt.axvline(x=1493, color='g', linestyle='-.', linewidth=3)
plt.axvline(x=1766, color='g', linestyle='-.', linewidth=3)
plt.axvline(x=2178, color='g', linestyle='-.', linewidth=3)
plt.axvline(x=2432, color='g', linestyle='-.', linewidth=3)
plt.axvline(x=2720, color='g', linestyle='-.', linewidth=3)
plt.title('Elevation vs. Distance')
plt.xlabel('Cumulative Distance (km)')
plt.ylabel('Elevation (m)')
plt.grid(True)
plt.show()
