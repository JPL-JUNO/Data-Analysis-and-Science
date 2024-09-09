"""
@File         : xlwings_pd.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-09 15:14:00
@Email        : cuixuanstephen@gmail.com
@Description  : xlwings 模块与 pandas 模块的交互
"""

import xlwings as xw
import pandas as pd

app = xw.App(visible=False)
workbook = app.books.add()
worksheet = workbook.sheets.add("新工作表")

df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
worksheet.range("A1").value = df
workbook.save("res/table.xlsx")
workbook.close()
app.quit()
