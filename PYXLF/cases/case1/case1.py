"""
@File         : case1.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-09 15:19:19
@Email        : cuixuanstephen@gmail.com
@Description  : 批量新建并保存工作簿
"""

import xlwings as xw

# 启动 xl 程序，但不新建工作簿
app = xw.App(visible=True, add_book=False)  # 会启动 xl 程序

# visible 表示启动 xl 程序后是否显示程序窗口，add_book 表示启动 xl 程序后是否新建工作簿

for i in range(6):
    workbook = app.books.add()  # 新建工作簿
    workbook.save(f"test{i}.xlsx")

    workbook.close()  # 关闭当前工作簿

app.quit()  # 退出 xl 程序
