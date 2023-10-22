"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-27 13:54:44
@Description: 
"""

from configparser import ConfigParser
cfg = ConfigParser()
# 读取自己的 token 文件（这样写主要是考虑隐私问题）
cfg.read('token.ini')
token = cfg.get("tushare", "token")
import tushare as ts
ts.set_token(token)
pro = ts.pro_api(token)
df = pro.daily(ts_code="00001.SZ", start_date="20180701", end_date="20180718")
