import pandas as pd
import numpy as np

import state
import config
from model import main
from offrace_solar_calc import calculate_energy

df_list = []

day_counter = 1
time_counter = 0
CONTROL_STOP_DURATION = 30 * 60
stop_gain = 0

for i in range(13):
    if state.DF_WayPoints[i+1] not in state.DayEnd_WayPoints:
        state.set_day_state(day_counter, i, time_counter)
        state.InitialBatteryCapacity = min(config.BatteryCapacity, stop_gain + state.InitialBatteryCapacity)
        outdf, timetaken = main(state.route_df)
        df_list.append(outdf)

        time_counter += timetaken
        stop_gain = calculate_energy(time_counter, time_counter + CONTROL_STOP_DURATION)
        time_counter += CONTROL_STOP_DURATION

    else:
        state.set_day_state(day_counter, i, time_counter)
        state.InitialBatteryCapacity = min(config.BatteryCapacity, stop_gain + state.InitialBatteryCapacity)

        outdf, timetaken = main(state.route_df)

        df_list.append(outdf)
        time_counter += timetaken

        stop_gain = calculate_energy(17*3600, 18*3600)
        stop_gain += calculate_energy(5*3600, 8*3600)
        day_counter += 1

dfnet = pd.concat(df_list)

dfnet.to_csv('run_dat.csv', index=False)
print("Written 5days data to `run_dat.csv`")
