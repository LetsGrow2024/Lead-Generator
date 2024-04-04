import openpyxl
from openpyxl import Workbook, load_workbook
book = load_workbook('menu.xlsx')
sheet = book.active
print(sheet)