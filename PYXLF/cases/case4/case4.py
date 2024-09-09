"""
@File         : case4.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-09 16:06:03
@Email        : cuixuanstephen@gmail.com
@Description  : 批量重命名多个工作簿
"""

# ！！！
# 本质上不需要如此复杂，仅仅需要更改文件名而已
# 这里的跳过 xl 临时文件是合理的，需要注意的


# 要重命名的工作簿名必须是有规律的，如表1、表2、表3；或者含有相同的关键字。

import os
import xlwings as xw

file_path = "./产品销售表"

file_list = os.listdir(file_path)

old_book_name = "销售表"
new_book_name = "分部产品销售表"

for i in file_list:
    if i.startswith("~$"):  # 判断是否有文件名以“~$”开头的临时文件
        continue
    new_file = i.replace(old_book_name, new_book_name)

    old_file_path = os.path.join(file_path, i)
    new_file_path = os.path.join(file_path, new_file)

    os.rename(old_file_path, new_file_path)  # 执行重命名

# 批量重命名多个工作簿中的同名工作表
# ！！！
# sheet name 应该是不能重复的
# file_path = "./信息表"
# file_list = os.listdir(file_path)
# old_sheet_name = "Sheet1"
# new_sheet_name = "员工信息"
# app = xw.App(visible=False, add_book=False)
# for i in file_list:
#     if i.startswith("~$"):
#         continue

#     old_file_path = os.path.join(file_path, i)
#     workbook = app.books.open(old_file_path)
#     for sheet in workbook.sheets:
#         if sheet.name == old_sheet_name:
#             sheet.name = new_sheet_name
#     workbook.save()

# app.quit()
