
# Model Settings
ModelMethod = "trust-constr"
InitialGuessVelocity = 35

RaceStartTime = 9 * 3600  # 9:00 am
RaceEndTime = (12 + 6) * 3600  # 6:00 pm

# ---------------------------------------------------------------------------------------------------------
# Car Data

# Battery
BatteryCapacity = 3055  # Wh
DeepDischargeCap = 0.20  # 20%

# Physical Attributes
R_In = 0.214 # inner radius of wheel
R_Out = 0.2785  # outer radius of wheel
Mass = 270 # kg
Wheels = 3
StatorRotorAirGap = 1.5 * 10**-3

# Resistive Coeff
CDA = 0.092
ZeroSpeedCrr = 0.0045
FrontalArea = 1  # m^2
Cd = 0.092  # coefficient of drag

# Solar Panel Data
PanelArea = 6  # m^2
PanelEfficiency = 0.19

# ---------------------------------------------------------------------------------------------------------
# Physical Constants
AirDensity = 1.192 # kg/m^3
g = GravityAcc = 9.81 # m/s^2
AirViscosity = 1.524 * 10**-5  # kinematic viscosity of air
Ta = 295

# ---------------------------------------------------------------------------------------------------------
# Car Constraints
MaxVelocity = 36  # m/s
MaxAcceleration  = 1.1  # m/s^2