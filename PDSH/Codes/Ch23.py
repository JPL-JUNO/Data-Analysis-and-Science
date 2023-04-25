"""
@Description: Working with Time Series
@Author:Stephen CUI
@Time: 2023-04-05 16:14:55
"""
from datetime import datetime
datetime(year=2023, month=4, day=5)

from dateutil import parser
date = parser.parse('4th of July, 2023')
date

date.strftime("%A")

import numpy as np

date = np.array('2023-04-05', dtype=np.datetime64)
date

date + np.arange(10)


np.datetime64('2023-04-05')
np.datetime64('2023-04-05 16:40')


import pandas as pd
date = pd.to_datetime('4th of July, 2021')
date

date.strftime('%A')

date + pd.to_timedelta(np.arange(12), 'D')

# Pandas Time Series: Indexing by Time
index = pd.DatetimeIndex(['2020-07-04', '2020-08-04',
                          '2021-07-04', '2021-08-04'])
data = pd.Series([0, 1, 2, 3], index=index)
data

data['2020-07-04':'2021-07-04']

data['2021']

dates = pd.to_datetime([datetime(2021, 7, 3), '4th of July, 2021',
                        '2021-Jul-6', '07-07-2021', '20210708'])
dates

dates.to_period('D')

dates - dates[0]


pd.date_range('2023-04-05', '2023-04-30')
pd.date_range('2023-04-05', periods=12)
pd.date_range('2023-04-05', periods=12, freq='H')


pd.period_range('2015-07', periods=8, freq='M')

pd.timedelta_range(0, periods=12, freq='H')

pd.timedelta_range(0, periods=12, freq='2H30T')

from pandas.tseries.offsets import BDay
pd.date_range('2015-07-01', periods=12, freq=BDay())

import yfinance as yf
from pandas_datareader import data as pdr
yf.pdr_override()

start_time = datetime(2018, 1, 1)
end_time = datetime(2022, 1, 1)
sp500 = pdr.get_data_yahoo('^GSPC', start=start_time, end=end_time)
sp500.head()

sp500 = sp500['Close']

import matplotlib.pyplot as plt
plt.style.use('ggplot')
sp500.plot()
plt.show()

sp500.plot(alpha=.3, style='y-')
sp500.resample('BA').mean().plot(style='b^:')
sp500.asfreq('BA').plot(style='ro--', alpha=.7)
plt.legend(['input', 'resample', 'asfreq'])
plt.show()


fig, ax = plt.subplots(2, sharex=True)
data = sp500.iloc[:20]
data.asfreq('D').plot(ax=ax[0], marker='o')
data.asfreq('D', method='bfill').plot(ax=ax[1], style='-o', label='back-fill')
data.asfreq('D', method='ffill').plot(
    ax=ax[1], style='--o', label='front-fill')
plt.legend()
plt.show()


sp500 = sp500.asfreq('D', method='pad')

ROI = 100 * (sp500.shift(-365) - sp500) / sp500
ROI.plot()
plt.ylabel('% Return on Investment after 1 year')
plt.show()


rolling = sp500.rolling(365, center=True)

data = pd.DataFrame({'input': sp500,
                     'one-year rolling_mean': rolling.mean(),
                     'one-year rolling_median': rolling.median()})
ax = data.plot(style=['-', '--', ':'])
ax.lines[0].set_alpha(.3)
plt.show()

# Example: Visualizing Seattle Bicycle Counts
