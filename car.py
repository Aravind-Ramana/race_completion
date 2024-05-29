import numpy as np

from config import (
    Mass, ZeroSpeedCrr, AirDensity, FrontalArea,
    Cd, CDA, R_In, R_Out, Ta,
    AirViscosity, StatorRotorAirGap,
    GravityAcc,
)

EPSILON = 10**-8

_CF_coeff1 = ((StatorRotorAirGap / R_Out) ** 0.167)
_CF_coeff2 = 2 * np.pi * R_Out / StatorRotorAirGap

_tou_rollingresistance = R_Out * Mass * GravityAcc * ZeroSpeedCrr
_tou_coeff1 = 0.5 * Cd * FrontalArea * AirDensity * (R_Out ** 3)
_tou_coeff1_wR = _tou_coeff1 / R_Out**2
_tou_coeff2 = 0.5 * AirDensity * np.pi * ((R_Out ** 5) - (R_In ** 5))
_tou_coeff2_wR = _tou_coeff2 / R_Out**2

_drag_coeff = 0.5 * CDA * AirDensity
_slope_coeff = Mass * GravityAcc

_windage_losses_coeff_wR2 = (170.4 * (10**-6)) / (R_Out **2)


def calculate_power(speed, acceleration, slope):
    speed2 = speed ** 2
    

    # v_rotor = omega * R_In  # circumferential speed of rotor
    # RN = v_rotor * R_Out / AirViscosity  # Reynolds number
    RN = speed * R_In/AirViscosity
    
    # if RN > 0.8 * 10**5:
    #     # Regime III
    #     # Cf = 0.08 / (((g / r_out) ** 0.167) * (RN ** 0.25)) 
    #     Cf = 0.08 / (_CF_coeff1 * (RN ** 0.25))
    # else:
    #     # Regime I
    #     # Cf = 2 * pi * r_out / (g * RN)
    #     Cf = _CF_coeff2 / RN

    Cf = np.where(RN > 0.8 * 10**5, 0.08 / (_CF_coeff1 * (RN ** 0.25)), _CF_coeff2 / RN)
    
    
    # t = r_out * ((m * 9.81 * u1) + (0.5 * Cd * a * rho * (omega ** 2) * (r_out ** 2))) + 0.5 * Cf * rho * pi * (omega ** 2) * ((r_out ** 5) - (r_in ** 5))
    tou = _tou_rollingresistance + (_tou_coeff1_wR + _tou_coeff2_wR * Cf) * (speed2)
    
    # Finding winding temperature
    Tw_i = Ta

    while True:
        # B = 1.32 - 1.2 * 10**-3 * (Ta / 2 + Tw_i / 2 - 293)
        B = 1.6716 - 0.0006 * (Ta + Tw_i)  # magnetic remanence
        i = 0.561 * B * tou  # RMS phase current

        # R = 0.0575 * (1 + 0.0039 * (Tw_i - 293))
        resistance = 0.00022425 * Tw_i - 0.00820525  # resistance of windings
        
        Pc = 3 * i ** 2 * resistance  # copper (ohmic) losses
        Pe = (9.602 * (10**-6) * ((B/R_Out) ** 2) / resistance) * speed2  # eddy current losses
        Tw = 0.455 * (Pc + Pe) + Ta
    
        cond = np.abs(Tw - Tw_i) < 0.001
        if np.all(cond):
            break

        Tw_i = np.where(cond, Tw_i, Tw)
        

    # Final eta calculations
    P_out = tou * speed / R_Out  # output power
    Pw = (speed2) * _windage_losses_coeff_wR2 # windage losses

    drag_force = _drag_coeff * ((speed-3.34)**2)#maximum possible drag
    P_acc = (drag_force + Mass * acceleration   # Adjusted for efficiency
            + _slope_coeff * np.sin(slope)) * speed

    P_net = P_out + Pw + Pc + Pe + P_acc
    return P_net.clip(0),P_out

def calculate_dt(start_speed, stop_speed, dx):
    dt = 2 * dx / (start_speed + stop_speed + EPSILON)
    return dt