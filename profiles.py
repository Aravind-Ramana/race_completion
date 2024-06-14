import numpy as np

from config import BatteryCapacity
import state
from car import calculate_dt, calculate_power
from solar import calculate_incident_solarpower

def extract_profiles(velocity_profile, segment_array, slope_array, lattitude_array, longitude_array,winds_array,winddir_array):
    start_speeds, stop_speeds = velocity_profile[:-1], velocity_profile[1:]
    ws=winds_array
    wd=winddir_array
    avg_speed = (start_speeds + stop_speeds) / 2
    dt = calculate_dt(start_speeds, stop_speeds, segment_array)
    acceleration = (stop_speeds - start_speeds) / dt

    P,_ = calculate_power(avg_speed, acceleration, slope_array,ws,wd)
    SolP = calculate_incident_solarpower(dt.cumsum() + state.TimeOffset, lattitude_array, longitude_array)

    energy_consumption = P * dt /3600
    energy_gain = SolP * dt /3600

    net_energy_profile = energy_consumption.cumsum() - energy_gain.cumsum()
    
    battery_profile = state.InitialBatteryCapacity - net_energy_profile
    battery_profile = np.concatenate((np.array([state.InitialBatteryCapacity]), battery_profile))

    battery_profile = battery_profile * 100 / (BatteryCapacity)

    distances = np.append([0], segment_array)

    return [
        distances,
        velocity_profile,
        np.concatenate((np.array([np.nan]), acceleration,)),
        battery_profile,
        np.concatenate((np.array([np.nan]), energy_consumption,)),
        np.concatenate((np.array([np.nan]), energy_gain)),
        np.concatenate((np.array([0]), dt.cumsum())) + state.TimeOffset,
    ]