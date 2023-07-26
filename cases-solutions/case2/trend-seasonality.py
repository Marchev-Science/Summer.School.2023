#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 08:49:45 2023

@author: dnt2
"""

import pandas as pd
import numpy as np
from scipy.signal import lombscargle
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import acf, pacf

# data_csv = 'https://raw.githubusercontent.com/mic00s/Summer-School-2023/main/extended_data/bus_data_w_iso_dates_and_delta_times.csv'
data_csv = '/home/dnt2/Spielplatz/Семково–2023/extended_data/bus_data_w_iso_dates_and_delta_times.csv'

datetime_columns = ['sched_1_355', 'sched_2_1035', 'sched_3_418', 'sched_4_2543',\
                'stop_1_355',  'stop_2_1035',  'stop_3_418',  'stop_4_2543']
    
data = pd.read_csv(data_csv, parse_dates=datetime_columns)



lags = 30

#  ===  ACF  ===

delta_t = 't_stop1_to_stop2'
time_series = data[delta_t].values
acf_values = acf(time_series, nlags=lags)

plot_acf(time_series, lags=lags)
plt.hlines( .2, 0, lags, color='k', ls='--', lw=1)
plt.hlines(-.2, 0, lags, color='k', ls='--', lw=1)
ax = plt.gca()
ax.set_ylim([-.25,1.05])
plt.xlabel('Lag (отчети)')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Function (ACF) of {}'.format(delta_t))


delta_t = 't_stop2_to_stop3'
time_series = data[delta_t].values
acf_values = acf(time_series, nlags=lags)

plot_acf(time_series, lags=lags)
plt.hlines( .2, 0, lags, color='k', ls='--', lw=1)
plt.hlines(-.2, 0, lags, color='k', ls='--', lw=1)
ax = plt.gca()
ax.set_ylim([-.25,1.05])
plt.xlabel('Lag (отчети)')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Function (ACF) of {}'.format(delta_t))


delta_t = 't_stop3_to_stop4'
time_series = data[delta_t].values
acf_values = acf(time_series, nlags=lags)

plot_acf(time_series, lags=lags)
plt.hlines( .2, 0, lags, color='k', ls='--', lw=1)
plt.hlines(-.2, 0, lags, color='k', ls='--', lw=1)
ax = plt.gca()
ax.set_ylim([-.25,1.05])
plt.xlabel('Lag (отчети)')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Function (ACF) of {}'.format(delta_t))

#  ===  PACF  ===

delta_t = 't_stop1_to_stop2'
time_series = data[delta_t].values
acf_values = pacf(time_series, nlags=lags)

plot_pacf(time_series, lags=lags)
plt.hlines( .2, 0, lags, color='k', ls='--', lw=1)
plt.hlines(-.2, 0, lags, color='k', ls='--', lw=1)
ax = plt.gca()
ax.set_ylim([-.25,1.05])
plt.xlabel('Lag (отчети)')
plt.ylabel('Partial Autocorrelation')
plt.title('Partial Autocorrelation Function (PACF) of {}'.format(delta_t))


delta_t = 't_stop2_to_stop3'
time_series = data[delta_t].values
pacf_values = pacf(time_series, nlags=lags)

plot_pacf(time_series, lags=lags)
plt.hlines( .2, 0, lags, color='k', ls='--', lw=1)
plt.hlines(-.2, 0, lags, color='k', ls='--', lw=1)
ax = plt.gca()
ax.set_ylim([-.25,1.05])
plt.xlabel('Lag (отчети)')
plt.ylabel('Partial Autocorrelation')
plt.title('Partial Autocorrelation Function (PACF) of {}'.format(delta_t))


delta_t = 't_stop3_to_stop4'
time_series = data[delta_t].values
pacf_values = pacf(time_series, nlags=lags)

plot_pacf(time_series, lags=lags)
plt.hlines( .2, 0, lags, color='k', ls='--', lw=1)
plt.hlines(-.2, 0, lags, color='k', ls='--', lw=1)
ax = plt.gca()
ax.set_ylim([-.25,1.05])
plt.xlabel('Lag (отчети)')
plt.ylabel('Partial Autocorrelation')
plt.title('Partial Autocorrelation Function (PACF) of {}'.format(delta_t))
