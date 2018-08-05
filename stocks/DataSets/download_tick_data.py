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



def download_data(comp_codes=[], start_date=datetime(2017, 6, 1),end_date=datetime.now(),split_data=False, sql_location=None, csv_location=None):
    
    if sql_location:
        from sqlalchemy import create_engine
        import sqlalchemy.types
        engine = create_engine('sqlite:///tick_data.db', echo=False)
    
    # get the raw prices from yahoo, auto retries on a 401 error
    raw_prices = pf.multi_price_fetch(codes_list=comp_codes, start_date=start_date, end_date=end_date)
    
    col_list = ['Symbol','Date','Open','High','Low','Close','Adj Close','Volume']
    df_skeleton = pd.DataFrame(columns = col_list)
    
    if not split_data:
        if csv_location:
            df_skeleton.to_csv(os.path.join(csv_location,'full_output.csv'),header=True,mode='w',index=False)
        
        if sql_location:
            df_skeleton.to_sql(
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
    
    counter = 0
    for symbol,tick_info in raw_prices.items():
        tick_info['Symbol'] = symbol
        tick_info = tick_info[col_list]
        tick_info['Date'] = pd.to_datetime(tick_info['Date'],infer_datetime_format=True)
    
        cols_to_convert_to_numeric = col_list.copy()
        cols_to_convert_to_numeric.remove('Symbol')
        cols_to_convert_to_numeric.remove('Date')
        
        tick_info[cols_to_convert_to_numeric] = tick_info[cols_to_convert_to_numeric].apply(pd.to_numeric,errors='coerce')
        
        if not split_data:
            if csv_location:
                tick_info.to_csv(os.path.join(csv_location,'full_output.csv'),header=False,mode='a',index=False)
            if sql_location:
                tick_info.to_sql('tick_data', con=engine,if_exists='append')
        
        else:
            if csv_location:
                tick_info.to_csv(os.path.join(csv_location,'{0}.csv'.format(symbol)),header=True, mode='w',index=False)
            if sql_location:
                tick_info.to_sql(
                symbol, 
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
                
                
        counter += 1
        print("Completed collecting tick info for {0}% of the companies required.".format((counter*100)/len(comp_codes)))

if __name__ == '__main__':
    import os
    
    st_dt = datetime(2010, 6, 1)
    
    sp = s_and_p_symbols()
    comp_codes = sp.get_s_and_p_symbols().tolist()
    
    comp_codes.append('^GSPC') # Append on SNP 500
    
    download_data(comp_codes = comp_codes, start_date = st_dt, split_data = True, sql_location='sqlite::///data/tick_data.db', csv_location=os.getcwd()+'/data')

