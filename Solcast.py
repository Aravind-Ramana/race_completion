import pandas as pd
import requests

# Solcast API credentials
SOLCAST_API_KEY = "ZzMo07Zx_N6ILAOf-dnfVRo3Fvyq2SvI"  # Replace with your Solcast API key
SOLCAST_API_URL = "https://api.solcast.com.au/data/live/radiation_and_weather"

# def download_solcast_data(latitude, longitude):
#     """
#     Download GHI, wind speed, and wind direction data from Solcast API for a given latitude and longitude.
    
#     Parameters:
#     latitude (float): Latitude of the location.
#     longitude (float): Longitude of the location.
    
#     Returns:
#     pd.DataFrame: DataFrame containing the downloaded data.
#     """
#     params = {
#         "latitude": latitude,
#         "longitude": longitude,
#         "hours": 168,  # Fetch data for 168 hours (7 days)
#         "output_parameters": "ghi,wind_speed_100m,wind_direction_100m",  # Requested parameters
#         "period": "PT30M",  # 30-minute intervals
#         "format": "csv",  # Download data in CSV format
#         "api_key": SOLCAST_API_KEY
#     }
#     response = requests.get(SOLCAST_API_URL, params=params)
#     if response.status_code == 200:
#         # Read the CSV data into a DataFrame
#         from io import StringIO
#         csv_data = StringIO(response.text)
#         df = pd.read_csv(csv_data)
#         return df
#     else:
#         print(f"Error downloading Solcast data: {response.status_code}")
#         return pd.DataFrame()  # Return an empty DataFrame if there's an error

# def add_solcast_data_to_csv(input_file, output_file):
#     """
#     Add GHI, wind speed, and wind direction data to the CSV file using Solcast API.
    
#     Parameters:
#     input_file (str): Path to the input CSV file.
#     output_file (str): Path to save the updated CSV file.
#     """
#     # Read the input CSV file
#     df = pd.read_csv(input_file)
    
#     # Initialize new columns with float64 data type
#     df["GHI"] = 0.0  # Use float instead of int
#     df["WIND_SPEED"] = 0.0  # Use float instead of int
#     df["WIND_DIRECTION"] = 0.0  # Use float instead of int
    
#     # Fetch data from Solcast API for each unique latitude and longitude
#     unique_locations = df[["Lattitude", "Longitude"]].drop_duplicates()
#     for _, location in unique_locations.iterrows():
#         latitude = location["Lattitude"]
#         longitude = location["Longitude"]
#         solcast_data = download_solcast_data(latitude, longitude)
        
#         if not solcast_data.empty:
#             # Get the most recent data (first row)
#             latest_data = solcast_data.iloc[10]
            
#             # Update the DataFrame with fetched data for all matching rows
#             mask = (df["Lattitude"] == latitude) & (df["Longitude"] == longitude)
#             df.loc[mask, "GHI"] = latest_data["ghi"]
#             df.loc[mask, "WIND_SPEED"] = latest_data["wind_speed_100m"]
#             df.loc[mask, "WIND_DIRECTION"] = latest_data["wind_direction_100m"]
    
#     # Save the updated DataFrame to a new CSV file
#     df.to_csv(output_file, index=False)
#     print(f"Updated data saved to {output_file}")

# # File paths
# input_file = "processed_route_data.csv"
# output_file = "updated_route_data.csv"

# # Add Solcast data to the CSV file
# add_solcast_data_to_csv(input_file, output_file)


def download_solcast_data(latitude, longitude):
    """
    Download GHI, wind speed, and wind direction data from Solcast API for a given latitude and longitude.
    
    Parameters:
    latitude (float): Latitude of the location.
    longitude (float): Longitude of the location.
    
    Returns:
    pd.DataFrame: DataFrame containing the downloaded data.
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hours": 168,  # Fetch data for 168 hours (7 days)
        "output_parameters": "ghi,wind_speed_100m,wind_direction_100m",  # Requested parameters
        "period": "PT30M",  #5-minute intervals
        "format": "csv",  # Download data in CSV format
        "api_key": SOLCAST_API_KEY
    }
    response = requests.get(SOLCAST_API_URL, params=params)
    if response.status_code == 200:
        # Read the CSV data into a DataFrame
        from io import StringIO
        csv_data = StringIO(response.text)
        df = pd.read_csv(csv_data)
        return df
    else:
        print(f"Error downloading Solcast data: {response.status_code}")
        return pd.DataFrame()  # Return an empty DataFrame if there's an error

def process_first_row(input_file, output_file):
    """
    Process only the first row of the input CSV file and fetch Solcast data.
    
    Parameters:
    input_file (str): Path to the input CSV file.
    output_file (str): Path to save the updated CSV file.
    """
    # Read the input CSV file
    df = pd.read_csv(input_file)
    
    # Check if the DataFrame is not empty
    if df.empty:
        print("Input CSV file is empty.")
        return
    
    # Get the first row
    first_row = df.iloc[6]
    latitude = first_row["Lattitude"]
    longitude = first_row["Longitude"]
    
    # Fetch data from Solcast API for the first row
    solcast_data = download_solcast_data(latitude, longitude)
    
    if not solcast_data.empty:
        # Get the most recent data (first row of Solcast data)
        print(solcast_data)
        latest_data = solcast_data.iloc[200]
        
        # Update the first row with fetched data
        df.at[0, "GHI"] = latest_data["ghi"]
        df.at[0, "WIND_SPEED"] = latest_data["wind_speed_100m"]
        df.at[0, "WIND_DIRECTION"] = latest_data["wind_direction_100m"]
    
    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Updated data saved to {output_file}")

# File paths
input_file = "processed_route_data.csv"
output_file = "updated_route_data.csv"

# Process only the first row
process_first_row(input_file, output_file)
