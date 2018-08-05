import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns; sns.set()

from data_exploration_stocks_data import scale

a_fundamental_data = pd.read_csv('data/indicators/A_indicators.csv')

# drop company_id column and pivot table
a_fundamental_data = a_fundamental_data.drop('company_id',axis=1)
a_fundamental_data = a_fundamental_data.set_index('indicator_id')
a_fundamental_data = a_fundamental_data.T





'''
fig, ax = plt.subplots()
plt.plot(scale(a_fundamental_data['AccountsPayableCurrent']))
plt.plot(scale(a_fundamental_data['AccountsReceivableNetCurrent']))
plt.plot(scale(a_fundamental_data['Assets']))

plt.xticks(rotation=45)
'''
corr = a_fundamental_data.corr()

#ax = sns.heatmap()
