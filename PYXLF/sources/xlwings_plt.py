"""
@File         : xlwings_plt.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-09 15:09:31
@Email        : cuixuanstephen@gmail.com
@Description  : xlwings 模块与 Matplotlib 模块的交互
"""

import xlwings as xw
import matplotlib.pyplot as plt

figure = plt.figure()
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
app = xw.App(visible=False)
workbook = app.books.add()
worksheet = workbook.sheets.add("新工作表")

worksheet.pictures.add(figure, name="图片 1", update=True, left=100)

workbook.save("./res/table_plt.xlsx")
workbook.close()
app.quit()
