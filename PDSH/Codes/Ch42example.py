import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.linear_model import LinearRegression

counts = pd.read_csv('data/FremontBridge.csv',
                     index_col='Date', parse_dates=True)
weather = pd.read_csv('data/SeattleWeather.csv',
                      index_col='DATE', parse_dates=True)

counts = counts[counts.index < '2020-01-01']
weather = weather[weather.index < '2020-01-01']
daily = counts.resample('d').sum()
daily['Total'] = daily.sum(axis=1)
daily = daily[['Total']]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for i in range(7):
    # onehot code
    daily[days[i]] = (daily.index.dayofweek == i).astype(float)

from pandas.tseries.holiday import USFederalHolidayCalendar
cal = USFederalHolidayCalendar()
holidays = cal.holidays('2012', '2020')
daily = daily.join(pd.Series(1, index=holidays, name='holiday'))
daily['holiday'].fillna(0, inplace=True)


def hours_of_daylight(date, axis=23.44, latitude=47.61):
    """compute the hours of daylight for the give date

    Args:
        date (_type_): _description_
        axis (float, optional): _description_. Defaults to 23.44.
        latitude (float, optional): _description_. Defaults to 47.61.
    """
    days = (date - datetime(2000, 12, 21)).days
    m = (1 - np.tan(np.radians(latitude)) *
         np.tan(np.radians(axis) * np.cos(days * 2 * np.pi / 365.25)))
    return 24. * np.degrees(np.arccos(1 - np.clip(m, 0, 2))) / 180.


daily['daylight_hrs'] = list(map(hours_of_daylight, daily.index))
# daily['daylight_hrs'].plot()

weather['Temp (F)'] = .5 * (weather['TMIN'] + weather['TMAX'])
weather['Rainfall (in)'] = weather['PRCP']
weather['dry day'] = (weather['PRCP'] == 0).astype(int)
daily = daily.join(weather[['Rainfall (in)', 'Temp (F)', 'dry day']])

daily['annual'] = (daily.index - daily.index[0]).days / 365

# daily.head()

daily.dropna(axis=0, how='any', inplace=True)
column_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun',
                'holiday', 'daylight_hrs', 'Rainfall (in)',
                'dry day', 'Temp (F)', 'annual']
X = daily[column_names]
y = daily['Total']

model = LinearRegression(fit_intercept=False)
model.fit(X, y)
daily['predicted'] = model.predict(X)
daily[['Total', 'predicted']].plot(alpha=.5)

params = pd.Series(model.coef_, index=X.columns)


from sklearn.utils import resample
np.random.seed(1)
err = np.std([model.fit(*resample(X, y)).coef_
              for i in range(1000)], 0)

pd.DataFrame({'effect': params.round(0),
              'uncertainty': err.round(0)})
