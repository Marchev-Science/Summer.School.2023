#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:00:08 2023

@author: dnt2
"""

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

data_csv = '/home/dnt2/Spielplatz/Семково–2023/extended_data/bus_data_w_iso_dates_and_delta_times.csv'

datetime_columns = ['sched_1_355', 'sched_2_1035', 'sched_3_418', 'sched_4_2543',\
                'stop_1_355',  'stop_2_1035',  'stop_3_418',  'stop_4_2543']

    
bus_data = pd.read_csv(data_csv, parse_dates=datetime_columns)


construction_start_date = datetime(year=2020, month=8, day=1)
construction_end_date   = datetime(year=2021, month=1, day=7, hour=12) 

fig, ax = plt.subplots()
ax.plot(bus_data.sched_1_355, bus_data.t_stop1_to_stop2, 'r')
# ax.axhline(np.mean(bus_data.t_stop1_to_stop2), c='k', ls='--', lw=1)
ax.axvline(construction_start_date, c="g", ls="--", lw=2)
ax.axvline(construction_end_date, c="g", ls="--", lw=2)
ax.set_title('Ремонтирани времена от stop_1_355 до stop_2_1035 (поради ремонт)')
ax.set_xlabel('sched_1_355')
ax.set_ylabel('Време в движение (секунди)')
ax.grid()


normal_ix = (bus_data.sched_1_355 < construction_start_date) | \
            (bus_data.sched_1_355 > construction_end_date)
normal_delta = bus_data.t_stop1_to_stop2.loc[normal_ix]

construction_ix = (bus_data.sched_1_355 >= construction_start_date) & \
                  (bus_data.sched_1_355 < construction_end_date)
construction_delta = bus_data.t_stop1_to_stop2.loc[construction_ix]

construction_sched_1_355 = bus_data.sched_1_355.loc[construction_ix]
# ax.plot(construction_sched_1_355, new_construciton_delta, color='grey')

normalized_construction_delta = (construction_delta-construction_delta.mean()) / construction_delta.std()
scaled_shifted_construction_delta = normalized_construction_delta * normal_delta.std() + normal_delta.mean()

ax.plot(construction_sched_1_355, scaled_shifted_construction_delta, color='grey')
ax.axhline(normal_delta.mean(), c='k', ls='--', lw=1)
plt.hlines(scaled_shifted_construction_delta.mean(),\
           xmin=construction_sched_1_355.iloc[0], xmax=construction_sched_1_355.iloc[-1], color='w', ls='--', lw=1)

t_stop1_to_stop2_original = bus_data.t_stop1_to_stop2.copy()
patched_t_stop1_to_stop2 = bus_data.t_stop1_to_stop2.copy()
patched_t_stop1_to_stop2.loc[construction_ix] = scaled_shifted_construction_delta


bus_data['t_stop1_to_stop2'] = patched_t_stop1_to_stop2
bus_data['t_stop1_to_stop2_original'] = t_stop1_to_stop2_original 

# --- Проверка ----
# ax.plot(bus_data.sched_1_355, patched_t_stop1_to_stop2, c='b')

# plt.figure()
# plt.plot(bus_data.t_stop1_to_stop2)
# plt.plot(bus_data.t_stop1_to_stop2_original)