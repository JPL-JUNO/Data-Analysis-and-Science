"""
@File         : case5.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-09 16:25:43
@Email        : cuixuanstephen@gmail.com
@Description  : 在多个工作簿中批量新增工作表
"""

import os
import xlwings as xw

file_path = "./销售表"
file_list = os.listdir(file_path)
sheet_name = "产品销售区域"

app = xw.App(visible=False, add_book=False)
for i in file_list:
    if i.startswith("~$"):
        continue
    file_paths = os.path.join(file_path, i)

    workbook = app.books.open(file_paths)

    sheet_names = [j.name for j in workbook.sheets]
    if sheet_name not in sheet_names:
        # 判断工作簿中是否不存在名为 “产品销售区域” 的工作表
        workbook.sheets.add(sheet_name)  # 如果不存在，则新增工作表 “产品销售区域”
    workbook.save()

app.quit()
