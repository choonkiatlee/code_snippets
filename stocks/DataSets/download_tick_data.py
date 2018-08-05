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
import pandas as pd

from sqlalchemy import create_engine
import sqlalchemy.types
engine = create_engine('sqlite:///tick_data.db', echo=False)

st_dt = datetime(2010, 6, 1)

sp = s_and_p_symbols()
comp_codes = sp.get_s_and_p_symbols().tolist()

# get the raw prices from yahoo, auto retries on a 401 error
raw_prices = pf.multi_price_fetch(codes_list=comp_codes, start_date=st_dt)

col_list = ['Symbol','Date','Open','High','Low','Close','Adj Close','Volume']
full_df = pd.DataFrame(columns = col_list)
full_df.to_csv('full_output.csv',header=True,mode='w',index=False)

full_df.to_sql(
    'tick_data', 
    con=engine,
    if_exists='replace',
    dtype={
        "Symbol": sqlalchemy.types.Text(),
        "Date":sqlalchemy.types.Date(),
        "Open":sqlalchemy.types.Float(),
        "High":sqlalchemy.types.Float(),
        "Low": sqlalchemy.types.Float(),
        "Close": sqlalchemy.types.Float(),
        "Adj Close": sqlalchemy.types.Float(),
        "Volume": sqlalchemy.types.BigInteger(),
        })


for symbol,tick_info in raw_prices.items():
    tick_info['Symbol'] = symbol
    tick_info = tick_info[col_list]
    tick_info['Date'] = pd.to_datetime(tick_info['Date'],infer_datetime_format=True)
    tick_info = pd.to_numeric(tick_info,errors='coerce')
    
    tick_info.to_csv('full_output.csv',header=False,mode='a',index=False)
    tick_info.to_sql('tick_data', con=engine,if_exists='append')

    

