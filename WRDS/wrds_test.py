# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 23:33:32 2018

@author: choon
"""

import wrds
db = wrds.Connection(wrds_username='manufact')

db.list_tables(library='comp')

db.describe_table(library='comp',table='funda')

db.raw_sql('select cusip,permno,date,bidlo,askhi from crsp.dsf LIMIT 100')

test = db.raw_sql(
        'select * from comp.funda where gvkey equals 126554 LIMIT 1')

test.to_csv('a_fundamentals.csv')