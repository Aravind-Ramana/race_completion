import config
import pandas as pd

# Model Settings
ModelMethod = "COBYLA"
InitialGuessVelocity =25

RaceStartTime = 8 * 3600  # 8:00 am
RaceEndTime = (17) * 3600  # 5:00 pm
DT = RaceEndTime - RaceStartTime

Day=1
TimeOffset = 0

# BatteryLevel
BatteryLevelWayPoints = [1, 0.4994, 0.808, 0.2543, 0.488, 0.2276, 0.408, 0.2410, 0.28, 0.2193, 0.20]
# Route DF
DF_WayPoints = [0, 57, 102, 169, 207, 254, 301, 371, 415, 464, 520]

InitialBatteryCapacity = None
FinalBatteryCapacity = None
route_df = None

def set_day_state(day_no, index_no, time_offset=0):
    global InitialBatteryCapacity, FinalBatteryCapacity, route_df, Day, TimeOffset
    Day = day_no
    TimeOffset = time_offset
    InitialBatteryCapacity = config.BatteryCapacity * BatteryLevelWayPoints[index_no] # Wh
    FinalBatteryCapacity = config.BatteryCapacity * BatteryLevelWayPoints[index_no+1]  # Wh
    route_df = pd.read_csv("processed_route_data.csv").iloc[DF_WayPoints[index_no]: DF_WayPoints[index_no+1]]
