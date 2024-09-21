"""
@File         : case6.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-10 11:26:31
@Email        : cuixuanstephen@gmail.com
@Description  : 批量打印工作簿
"""

import os
import xlwings as xw

file_path = "./公司"
file_list = os.listdir(file_path)

app = xw.App(visible=False, add_book=False)
for i in file_list:
    if i.startswith("~$"):
        continue
    file_paths = os.path.join(file_path, i)

    workbook = app.books.open(file_paths)

    workbook.api.PrintOut()  # 打印工作簿

app.quit()
