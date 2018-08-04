#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 17:34:23 2018

@author: ckl41
"""


### This package requires aiohttp to be installed ###

import py_yahoo_prices.price_fetcher as pf
from datetime import datetime
from get_s_and_p_data import s_and_p_symbols


st_dt = datetime(2017, 6, 1)

sp = s_and_p_symbols()
comp_codes = sp.get_s_and_p_symbols().tolist()



# get the raw prices from yahoo, auto retries on a 401 error
raw_prices = pf.multi_price_fetch(codes_list=comp_codes, start_date=st_dt)

for symbol,tick_info in raw_prices.items():
    tick_info.to_csv('{0}.csv'.format(symbol))