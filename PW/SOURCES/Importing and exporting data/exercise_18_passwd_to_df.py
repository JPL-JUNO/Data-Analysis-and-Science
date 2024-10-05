"""
@File         : exercise_18_passwd_to_df.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-10-05 14:51:09
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import pandas as pd

df = pd.read_csv(
    "../../DATA/linux-etc-passwd.txt",
    sep=":",
    comment="#",
    header=None,
    names=["username", "password", "userid", "groupid", "name", "homedir", "shell"],
    skip_blank_lines=True,
)
