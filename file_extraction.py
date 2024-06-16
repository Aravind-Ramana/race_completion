import csv

# Define the input and output file names
input_filename = 'test_wind.csv'
output_filename = 'wind.csv'

# Read the input data
with open(input_filename, mode='r') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

# Prepare the output data
output_data = []
for row in rows:
    wind_speed = row['Avg Velocity']
    wind_direction = row['Directions']
    repetitions = int(row['No of Repetitons'])
    
    for j in range(repetitions):
        output_data.append([wind_speed, wind_direction])

# Write the output data to the new CSV file
with open(output_filename, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['WindSpeed(m/s)', 'Winddirection(frmnorth)'])
    writer.writerows(output_data)

print(f"Data successfully written to {output_filename}")
