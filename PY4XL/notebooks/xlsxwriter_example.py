import datetime as dt
import xlsxwriter
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from sources import excel

book = xlsxwriter.Workbook("res/xlsxwriter.xlsx")
sheet = book.add_worksheet("Sheet1")

sheet.write("A1", "Hello 1")
sheet.write(1, 0, "Hello 2")

formatting = book.add_format(
    {
        "font_color": "#FF0000",
        "bg_color": "#FFFF00",
        "bold": True,
        "align": "center",
        "border": 1,
        "border_color": "#FF0000",
    }
)

sheet.write("A3", "Hello 3", formatting)

number_format = book.add_format({"num_format": "0.00"})
sheet.write("A4", 3.3333, number_format)

date_format = book.add_format({"num_format": "mm/dd/yy"})
sheet.write("A5", dt.date(2016, 10, 13), date_format)

sheet.write("A6", "=SUM(A4, 2)")

sheet.insert_image(0, 2, "images/python.png")

data = [[None, "North", "South"], ["Last Year", 2, 5], ["This Year", 3, 6]]
excel.write(sheet, data, "A10")

chart = book.add_chart({"type": "column"})
chart.set_title({"name": "Sales Per Region"})
chart.add_series(
    {
        "name": "=Sheet1!A11",
        "categories": "=Sheet1B10:C10",
        "values": "=Sheet1!B11:C11",
    }
)
chart.add_series(
    {
        "name": "=Sheet1!A12",
        "categories": "=Sheet1!B10:C10",
        "values": "=Sheet1!B12:C12",
    }
)

chart.set_x_axis({"name": "Regions"})
chart.set_y_axis({"name": "Sales"})
sheet.insert_chart("A15", chart)
book.close()
