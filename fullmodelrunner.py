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

for i in range(10):
    if i % 2 == 0:
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

        stop_time = state.DT - (time_counter % state.DT)
        stop_gain = calculate_energy(time_counter, time_counter + stop_time)
        time_counter += stop_time

        day_counter += 1

dfnet = pd.concat(df_list)

dfnet.to_csv('run_dat.csv', index=False)
print("Written 5days data to `run_dat.csv`")
