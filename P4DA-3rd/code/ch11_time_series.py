"""
@File         : ch11_time_series.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-04-07 01:15:54
@Email        : cuixuanstephen@gmail.com
@Description  : 时间序列
"""

import numpy as np
import pandas as pd
from datetime import datetime

now = datetime.now()
now
now.year, now.month, now.day
delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
delta
