# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 13:09:29 2018

@author: choon
"""

import requests

s = requests.Session() 

text = """
<ul id='ser' class='list_style'>
    	<li signature='19'><label  class='selected'>Aluminum Cash Price (US$ per tonne)</label></li>
    	<li signature='69'><label  class=''>Butter Cash Price (pound)</label></li>
    	<li signature='76'><label  class=''>Cattle Feeder nf (cents per lb)</label></li>
    	<li signature='7'><label  class=''>Cattle Live nf (cents per lb)</label></li>
    	<li signature='72'><label  class=''>Cement Shipments-Masonry (metric tons)</label></li>
    	<li signature='71'><label  class=''>Cement Shipments-Portland (metric tons)</label></li>
    	<li signature='23'><label  class=''>Cocoa nf ($ per ton)</label></li>
    	<li signature='8'><label  class=''>Coffee nf (cents per lb)</label></li>
    	<li signature='9'><label  class=''>Copper High Grade nf ($ per lb)</label></li>
    	<li signature='20'><label  class=''>Copper High Grade Spot Price ($ per lb)</label></li>
    	<li signature='10'><label  class=''>Corn nf (cents per bushel)</label></li>
    	<li signature='11'><label  class=''>Cotton nf (cents per lb)</label></li>
    	<li signature='68'><label  class=''>Cottonseed Cash Price (ton)</label></li>
    	<li signature='3'><label  class=''>CRB Futures Index</label></li>
    	<li signature='4'><label  class=''>CRB Spot Price Index</label></li>
    	<li signature='38'><label  class=''>Crude Oil Brent Spot Price ($ per bbl)</label></li>
    	<li signature='28'><label  class=''>Crude Oil nf ($ per bbl)</label></li>
    	<li signature='51'><label  class=''>Diesel LA spot ($ per gallon)</label></li>
    	<li signature='53'><label  class=''>Diesel NY Harbor spot ($ per gallon)</label></li>
    	<li signature='52'><label  class=''>Diesel US Gulf Coast spot ($ per gallon)</label></li>
    	<li signature='70'><label  class=''>Eggs Cash Price (dozen)</label></li>
    	<li signature='33'><label  class=''>Ethanol nf ($ per gal)</label></li>
    	<li signature='30'><label  class=''>Gasoline NY Harbor RBOB nf ($ per gal)</label></li>
    	<li signature='44'><label  class=''>Gasoline RBOB LA spot ($ per gallon)</label></li>
    	<li signature='39'><label  class=''>Gasoline Regular NY Harbor spot ($ per gallon)</label></li>
    	<li signature='40'><label  class=''>Gasoline Regular US Gulf Coast spot ($ per gallon)</label></li>
    	<li signature='6'><label  class=''>Gold London Cash Price (US$ per troy oz)</label></li>
    	<li signature='12'><label  class=''>Gold nf (100 oz )</label></li>
    	<li signature='27'><label  class=''>Heating Oil nf ($ per gal)</label></li>
    	<li signature='47'><label  class=''>Heating Oil NY Harbor spot ($ per gallon)</label></li>
    	<li signature='13'><label  class=''>Hogs nf (cents per lb)</label></li>
    	<li signature='37'><label  class=''>Interest Rate Swaps 10 Yr (CBT)</label></li>
    	<li signature='36'><label  class=''>Intrinsic Research Equity Risk Premium</label></li>
    	<li signature='75'><label  class=''>Iron Ore Production (thousand metric tons)</label></li>
    	<li signature='74'><label  class=''>Iron Ore Shipments (thousand metric tons)</label></li>
    	<li signature='55'><label  class=''>Jet Fuel US Gulf Coast spot ($ per gallon)</label></li>
    	<li signature='77'><label  class=''>Lead Cash Price (US$ per tonne)</label></li>
    	<li signature='14'><label  class=''>Lumber nf ($ per 110,000 bd ft)</label></li>
    	<li signature='67'><label  class=''>Lumber Spot Price ($ per 110,000 bd ft)</label></li>
    	<li signature='35'><label  class=''>Milk nf (cents per lb)</label></li>
    	<li signature='5'><label  class=''>Natural Gas Henry Hub Spot Price ($ per MMBtu)</label></li>
    	<li signature='29'><label  class=''>Natural Gas nf ($ per MMBtu)</label></li>
    	<li signature='21'><label  class=''>Nickel Cash Price (US$ per tonne)</label></li>
    	<li signature='34'><label  class=''>Oats nf (cents per bushel)</label></li>
    	<li signature='25'><label  class=''>Orange Juice nf (cents per lb)</label></li>
    	<li signature='2'><label  class=''>Palladium Spot Price ($ per troy oz)</label></li>
    	<li signature='26'><label  class=''>Platinum nf ($ per troy oz)</label></li>
    	<li signature='1'><label  class=''>Platinum Spot Price ($ per troy oz)</label></li>
    	<li signature='15'><label  class=''>Pork Bellies nf (cents per lb)</label></li>
    	<li signature='64'><label  class=''>Propane Texas spot ($ per gallon)</label></li>
    	<li signature='16'><label  class=''>Silver nf ($ per troy oz)</label></li>
    	<li signature='32'><label  class=''>Soybean Oil 1-Yr Fut (cents per lb)</label></li>
    	<li signature='31'><label  class=''>Soybean Oil nf (cents per lb)</label></li>
    	<li signature='17'><label  class=''>Soybeans nf (cents per bushel)</label></li>
    	<li signature='73'><label  class=''>Stainless Steel Production (metric tons)</label></li>
    	<li signature='22'><label  class=''>Steel Scrap Cash Price US ($ per gross ton)</label></li>
    	<li signature='24'><label  class=''>Sugar World nf (cents per lb)</label></li>
    	<li signature='18'><label  class=''>Wheat nf (cents per bushel)</label></li>
	</ul>
"""

output_dict = {}


import re
m = re.findall("'[0-9]+'", text)
m = [int(number.replace("'",'')) for number in m]

output_dict[1] = m


