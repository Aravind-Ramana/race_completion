import numpy as np

from config import BatteryCapacity, DeepDischargeCap, MaxVelocity, Mass, MaxCurrent, BusVoltage
import state
from car import calculate_dt, calculate_power
from solar import calculate_incident_solarpower

SafeBatteryLevel = BatteryCapacity * (DeepDischargeCap)
MaxPower = MaxCurrent * BusVoltage

# Bounds for the velocity
def get_bounds(N):
    return ([(0, 0)] + [(0.01, MaxVelocity)]*(N-2) + [(0, 0)])

def objective(velocity_profile, segment_array):
    dt = calculate_dt(velocity_profile[:-1], velocity_profile[1:], segment_array)
    return np.sum(dt)

def battery_acc_constraint_func(v_prof, segment_array, slope_array, lattitude_array, longitude_array,ws,wd):
    start_speeds, stop_speeds = v_prof[:-1], v_prof[1:]
    
    avg_speed = (start_speeds + stop_speeds) / 2
    dt = calculate_dt(start_speeds, stop_speeds, segment_array)
    acceleration = (stop_speeds - start_speeds) / dt

    P, PO = calculate_power(avg_speed, acceleration, slope_array,ws,wd)
    SolP = calculate_incident_solarpower(dt.cumsum() + state.TimeOffset, lattitude_array, longitude_array)

    energy_consumption = ((P - SolP) * dt).cumsum() / 3600
    battery_profile = state.InitialBatteryCapacity - energy_consumption - SafeBatteryLevel

    return np.min(battery_profile), MaxPower - np.max(P)

def final_battery_constraint_func(v_prof, segment_array, slope_array, lattitude_array, longitude_array,ws,wd):
    start_speeds, stop_speeds = v_prof[:-1], v_prof[1:]
    
    avg_speed = (start_speeds + stop_speeds) / 2
    dt = calculate_dt(start_speeds, stop_speeds, segment_array)
    acceleration = (stop_speeds - start_speeds) / dt

    P, _= calculate_power(avg_speed, acceleration, slope_array,ws,wd)
    SolP = calculate_incident_solarpower(dt.cumsum() + state.TimeOffset, lattitude_array, longitude_array)

    energy_consumption = ((P - SolP) * dt).cumsum() / 3600
    final_battery_lev = state.InitialBatteryCapacity - energy_consumption[-1] - state.FinalBatteryCapacity
    return final_battery_lev, -final_battery_lev