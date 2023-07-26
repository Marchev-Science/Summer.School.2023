#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 09:01:10 2023

Източник: https://stackoverflow.com/questions/34428886/discrete-fourier-transformation-from-a-list-of-x-y-points/34432195#34432195

@author: dnt2
"""

import pandas as pd
import numpy as np
from scipy.signal import lombscargle
import matplotlib.pyplot as plt
from datetime import timedelta

def timestamp_s(x):
    '''
    

    Параметри
    ----------
    x : datetime.datetime
        Астрономическо време от една клетка -- кога тръгва или пристига автобуса

    Резултати
    -------
    float
        timestamp в секунди

    '''
    # Изваждаме 2 часа заради разликите прин интерпретиране на времето между Ехсе1 и Рутноп
    two_hours = timedelta(hours=2)
    return (x-two_hours).timestamp()

if __name__ == "__main__":

    data_csv = '/home/dnt2/Spielplatz/Семково–2023/extended_data/bus_data_w_iso_dates_and_delta_times.csv'
    
    datetime_columns = ['sched_1_355', 'sched_2_1035', 'sched_3_418', 'sched_4_2543',\
                    'stop_1_355',  'stop_2_1035',  'stop_3_418',  'stop_4_2543']
    
    datetime_in_seconds_columns = ['sched_1_355_s', 'sched_2_1035_s', 'sched_3_418_s', 'sched_4_2543_s',\
                    'stop_1_355_s',  'stop_2_1035_s',  'stop_3_418_s',  'stop_4_2543_s']

        
    data = pd.read_csv(data_csv, parse_dates=datetime_columns)
    
    for col, col_s in zip(datetime_columns, datetime_in_seconds_columns):
        data[col_s] = pd.DataFrame(data[col].dt.to_pydatetime()).applymap(timestamp_s)[0]
        
    data.to_csv('/home/dnt2/Spielplatz/Семково–2023/extended_data/bus_data_w_iso_dates_and_delta_times.csv', index=False)

    delta = 't_stop1_to_stop2'
    x = data['sched_1_355_s']
    y = data[delta]
    
    # # Минимален sampling интервал
    dxmin = np.diff(x).min()
    duration = x.max() - x.min()
    
    n = len(x)
    freqs = np.linspace(1/duration, n/duration, 5*n)
    periodogram = lombscargle(x, y, freqs)
    
    kmax = periodogram.argmax()
    # print("%8.3f" % (freqs[kmax],))
    
    plt.figure()
    p = np.sqrt(4*periodogram/(5*n))
    plt.plot(freqs, p/p.max(), c='r', lw=1)
    plt.xlabel('Frequency (rad/s)')
    plt.grid()
    # plt.axvline(freqs[kmax], color='r', alpha=0.25)
    plt.title('Lomb-Scargle nериодограма на {}'.format(delta))
    

    delta = 't_stop2_to_stop3'
    x = data['sched_2_1035_s']
    y = data[delta]
    
    # # Минимален sampling интервал
    dxmin = np.diff(x).min()
    duration = x.max() - x.min()
    
    n = len(x)
    freqs = np.linspace(1/duration, n/duration, 5*n)
    periodogram = lombscargle(x, y, freqs)
    
    kmax = periodogram.argmax()
    # print("%8.3f" % (freqs[kmax],))
    
    plt.figure()
    p = np.sqrt(4*periodogram/(5*n))
    plt.plot(freqs, p/p.max(), c='g', lw=1)
    plt.xlabel('Frequency (rad/s)')
    plt.grid()
    # plt.axvline(freqs[kmax], color='r', alpha=0.25)
    plt.title('Lomb-Scargle nериодограма на {}'.format(delta))
    
    
    delta = 't_stop3_to_stop4'
    x = data['sched_3_418_s']
    y = data[delta]
    
    # # Минимален sampling интервал
    dxmin = np.diff(x).min()
    duration = x.max() - x.min()
    
    n = len(x)
    freqs = np.linspace(1/duration, n/duration, 5*n)
    periodogram = lombscargle(x, y, freqs)
    
    # kmax = periodogram.argmax()
    # print("%8.3f" % (freqs[kmax],))
    
    plt.figure()
    p = np.sqrt(4*periodogram/(5*n))
    plt.plot(freqs, p/p.max(), c='b', lw=1)
    plt.xlabel('Frequency (rad/s)')
    plt.grid()
    # plt.axvline(freqs[kmax], color='r', alpha=0.25)
    plt.title('Lomb-Scargle nериодограма на {}'.format(delta))


