"""
@File         : ch01_generating_summary_statistics.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-21 17:07:40
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import numpy as np
import pandas as pd
from scipy import stats

covid_data = pd.read_csv(
    "DATA/covid-data.csv",
    usecols=["iso_code", "continent", "location", "date", "total_cases", "new_cases"],
)

data_mean = np.mean(covid_data.new_cases)
data_median = np.median(covid_data.new_cases)
data_mode = stats.mode(covid_data.new_cases, keepdims=False)
data_variance = np.var(covid_data.new_cases)
data_std = np.std(covid_data.new_cases)
data_max, data_min = np.max(covid_data.new_cases), np.min(covid_data.new_cases)
data_percentile = np.percentile(covid_data.new_cases, 0.75)
data_quartile = np.quantile(covid_data.new_cases, [0.25, 0.5, 0.75])
data_iqr = stats.iqr(covid_data.new_cases)
