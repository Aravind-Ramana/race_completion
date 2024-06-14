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
# BatteryLevelWayPoints = [1, 0.4994, 0.5, 0.2543, 0.488, 0.2276, 0.408, 0.2410, 0.27, 0.2393, 0.22]
# BatteryLevelWayPoints = [1,0.44,0.51,0.5,0.2543,0.488,0.48,0.3276,0.408,0.39,0.2410,0.28,0.33,0.22]
BatteryLevelWayPoints = [1,0.44,0.51,0.5,0.2543,0.488,0.48,0.3276,0.408,0.39,0.2410,0.299,0.43,0.22]
# Route DF
# DF_WayPoints = [0, 57, 102, 169, 207, 254, 301, 371, 415, 464, 520]
# DF_WayPoints = [0, 57, 102, 109, 169, 207, 213, 254, 301, 308, 371, 415, 464, 520]
DF_WayPoints = [0, 57, 102, 109, 169, 207, 213, 254, 301, 308, 371, 415, 464, 520]
# DF_WayPoints = [0, 57*2, 102*2, 109*2, 169*2, 207*2, 213*2, 254*2, 301*2, 308*2, 371*2, 415*2, 464*2, 520*2]
DayEnd_WayPoints = [109, 213, 308, 415, 520]
# DayEnd_WayPoints = [109*2, 213*2, 308*2, 415*2, 520*2]

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
