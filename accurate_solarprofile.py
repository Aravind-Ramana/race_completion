import numpy as np
from datetime import datetime, timedelta
from config import PanelArea, PanelEfficiency, RaceStartTime, RaceEndTime

# Constants
G_s = 1366  # Solar constant in W/m^2
G_s_prime = 0.7 * G_s  # Adjusted solar constant for clear day
_power_coeff = PanelArea * PanelEfficiency
DT = RaceEndTime - RaceStartTime

# Function to calculate the nth day of the year
def day_of_year(date):
    return date.timetuple().tm_yday

# Function to calculate B
def calculate_B(N):
    return (N - 1) * 360 / 365

# Function to calculate the equation of time (E)
def equation_of_time(B):
    return 229.2 * (0.00018865 * np.cos(np.radians(B)) - 0.0032077 * np.sin(np.radians(B)) +
                    0.041016 * np.cos(np.radians(2 * B)) - 0.048093 * np.sin(np.radians(2 * B)))

# Function to calculate solar local time (T_s)
def solar_local_time(standard_time, longitude, standard_meridian, E):
    return standard_time + (4 * (standard_meridian - longitude) + E) / 60

# Function to calculate hour angle (ω)
def hour_angle(T_s):
    return 15 * (T_s - 12)

# Function to calculate sun declination angle (δ)
def sun_declination_angle(N):
    return 23.45 * np.sin(np.radians(360 / 365 * (284 + N)))

# Function to calculate solar irradiance (G_b)
def solar_irradiance(G_s_prime, latitude, declination, hour_angle):
    latitude_rad = np.radians(latitude)
    declination_rad = np.radians(declination)
    hour_angle_rad = np.radians(hour_angle)
    return G_s_prime * (np.cos(latitude_rad) * np.cos(declination_rad) * np.cos(hour_angle_rad) + np.sin(latitude_rad) * np.sin(declination_rad))

# Main function to calculate incident solar power
def calculate_incident_solarpower(globaltime, latitude_array, longitude_array):
    # Assume a fixed date for simplicity, can be changed as needed
    date = datetime.now()

    # Calculate the day of the year
    N = day_of_year(date)
    B = calculate_B(N)

    # Calculate the standard meridian
    standard_meridian = 15 * (longitude_array / 15).astype(int)

    # Calculate the equation of time
    E = equation_of_time(B)

    time = globaltime % DT

    # Calculate the standard time in hours (decimal)
    standard_time = time / 3600

    # Calculate the solar local time for each point
    T_s = solar_local_time(standard_time, longitude_array, standard_meridian, E)
    # Calculate the hour angle for each point
    omega = hour_angle(T_s)
    # Calculate the sun declination angle
    delta = sun_declination_angle(N)
    # Calculate the solar irradiance for each point
    G_b = solar_irradiance(G_s_prime, latitude_array, delta, omega)
    
    return G_b * _power_coeff

# # Example usage
# if __name__ == "__main__":
#     # Example input
#     latitude_array = np.array([35.6895, 34.0522])  # Example latitudes
#     longitude_array = np.array([139.6917, -118.2437])  # Example longitudes
#     globaltime = 3600  # Example global time in seconds

#     # Calculate the incident solar power
#     power = calculate_incident_solarpower(globaltime, latitude_array, longitude_array)
#     print(f"Incident Solar Power: {power} W")

