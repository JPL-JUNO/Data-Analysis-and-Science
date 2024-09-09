"""
@File         : case3.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-09 15:57:48
@Email        : cuixuanstephen@gmail.com
@Description  : 批量重命名一个工作簿中的所有工作表
"""

import xlwings as xw

app = xw.App(visible=False, add_book=False)
workbook = app.books.open("./统计表.xlsx")
worksheets = workbook.sheets  # 获取工作簿中的所有工作表

# for i in range(len(worksheets))[:5]: # 选择部分工作表
for i in range(len(worksheets)):
    worksheets[i].name = worksheets[i].name.replace("销售", "")

workbook.save("统计表_修改后.xlsx")
app.quit()
