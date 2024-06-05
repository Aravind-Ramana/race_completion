import pandas as pd
import numpy as np

import state
from model import main

df_list = []

for i in range(1, 6):
    state.set_day_state(i)
    df_list.append(main(state.route_df))

dfnet = pd.concat(df_list)

dfnet.to_csv('run_dat.csv', index=False)
print("Written 5days data to `run_dat.csv`")

