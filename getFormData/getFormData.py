#!usr/bin/env python3
# getFormData.py - Downloads emails from google sheets
# file with form answers.

import ezsheets

sheet_url = '1q2sQt8WicsMBAE9OTDaGHGtkTXHXzLBdj7AS72OTRpw'

ss = ezsheets.Spreadsheet(sheet_url)
sheet = ss[0]  # Get first worksheet
email_column = sheet.getColumn(2)  # Get all rows from column B
for i in sheet.getColumn(2):
    if i != '':  # If cell not empty
        print(i)
