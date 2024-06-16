import csv

# Define file names
wind_file = 'test_wind.csv'
processed_route_file = 'processed_route_data1.csv'
output_file = 'processed_route_data.csv'

# Step 1: Read wind data from wind.csv
wind_data = []
with open(wind_file, mode='r') as wf:
    wind_reader = csv.reader(wf)
    next(wind_reader)  # Skip header
    for row in wind_reader:
        
        wind_data.append([row[0],row[2]])

# Step 2: Read route data from processed_route_data1.csv
route_data = []
with open(processed_route_file, mode='r') as rf:
    route_reader = csv.reader(rf)
    headers = next(route_reader)  # Read headers
    route_data = [row for row in route_reader]

# Step 3: Replace the last two columns with wind data
for i, row in enumerate(route_data):
    if i < len(wind_data):
        row[-2:] = wind_data[i]
    else:
        print(f"Warning: More route data than wind data. Row {i} unchanged.")

# Step 4: Write the modified data to processed_route_data.csv
with open(output_file, mode='w', newline='') as of:
    writer = csv.writer(of)
    writer.writerow(headers)  # Write headers
    writer.writerows(route_data)  # Write modified data

print(f"Data successfully written to {output_file}")
