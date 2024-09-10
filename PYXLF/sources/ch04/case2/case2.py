"""
@File         : case2.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-09 15:30:33
@Email        : cuixuanstephen@gmail.com
@Description  : 批量打开一个文件夹下的所有工作簿
"""

import os
import xlwings as xw
from pathlib import Path

file_list = Path("./table").glob("*.xlsx")

# file_path = "./table"
# file_list = os.listdir(file_path)
app = xw.App(visible=True, add_book=False)

# for i in file_list:
#     if os.path.splitext(i)[1] == ".xlsx":
#         app.books.open(file_path + "\\" + i)
# 上面注释的原书代码，修改后
# for files in file_list:
#     app.books.open(files)

# ！！！
# 其实全选 xl 文件，然后 enter 也可以全部一次性打开

# 输出文件下的全部文件名，不含路径
# file_path = "./table"
# for i in os.listdir(file_path):
#     print(i)
