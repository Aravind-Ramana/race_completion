import config
import pandas as pd

# Model Settings
ModelMethod = "COBYLA"
InitialGuessVelocity =25

RaceStartTime = 8 * 3600  # 8:00 am
RaceEndTime = (17) * 3600  # 5:00 pm

Day=1

# BatteryLevel
BatteryLevelWayPoints = [1, 0.808, 0.488, 0.408, 0.28, 0.2]
# Route DF
DF_WayPoints = [0, 110, 220, 330, 440, 550]

InitialBatteryCapacity = None
FinalBatteryCapacity = None
route_df = None

def set_day_state(day_no):
    global InitialBatteryCapacity, FinalBatteryCapacity, route_df, Day
    Day = day_no
    InitialBatteryCapacity = config.BatteryCapacity * BatteryLevelWayPoints[Day-1] # Wh
    FinalBatteryCapacity = config.BatteryCapacity * BatteryLevelWayPoints[Day]  # Wh
    route_df = pd.read_csv("processed_route_data.csv").iloc[DF_WayPoints[Day-1]: DF_WayPoints[Day]]

set_day_state(Day)