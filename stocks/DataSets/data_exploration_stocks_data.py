#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 15:22:24 2018

@author: ckl41
"""

import pandas as pd
import numpy as np

snp_tick_data = pd.read_csv('data/^GSPC.csv')
a_tick_data = pd.read_csv('data/A.csv')

def normalise(data):
    return (data-data.mean())/data.std()

def scale(data,start=0,stop=1):
    data_boundaries = data.max() - data.min()
    return ((data-data.min()) / data_boundaries)* (stop-start) + start
    
a_tick_data['a_normalised'] = scale(a_tick_data['Open'])
snp_tick_data['snp_normalised'] = scale(snp_tick_data['Open'])
a_tick_data['a_vol_normalised'] = scale(a_tick_data['Volume'])
a_tick_data['a_log_returns'] = np.log(1 + a_tick_data['Open'].pct_change())
a_tick_data['a_returns'] = a_tick_data['Open'].pct_change()

snp_tick_data['snp_normalised'].plot(legend=True)
a_tick_data['a_normalised'].plot(legend=True)
#a_tick_data['a_vol_normalised'].plot(legend=True)
a_tick_data['a_log_returns'].plot(legend=True)
a_tick_data['a_returns'].plot(legend=True)
