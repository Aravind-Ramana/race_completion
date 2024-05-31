import pandas as pd
from config import (
    Mass, ZeroSpeedCrr, AirDensity, FrontalArea,
    Cd, CDA, R_In, R_Out, Ta,
    AirViscosity, StatorRotorAirGap,
    GravityAcc,
)
#import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('run_dat.csv')

# Constants
_drag_coeff = 0.5 * CDA * AirDensity  # You need to define CDA and AirDensity
reference_speed = 3.34

# Calculate drag force for each data point
data['DragForce'] = _drag_coeff * ((data['Velocity'] - reference_speed) ** 2)

# Calculate frictional loss for each data point
data['FrictionalLoss'] = _drag_coeff * ((data['Velocity'] - reference_speed) ** 2) * data['Velocity']

# Calculate net drag by summing all drag forces
net_drag = data['DragForce'].sum()

# Calculate net frictional loss
net_frictional_loss = data['FrictionalLoss'].sum()

# Print the results
print("Net Drag:", net_drag)
print("Net Frictional Loss:", net_frictional_loss)
