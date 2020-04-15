#!usr/bin/env python3
# textFilesToSpreadsheet.py - Adding text from files to individual columns in
# Excel spreadsheet. One line per row. Filenames are provided as CL arguments.

import openpyxl
import sys

files = [i for i in sys.argv[1:]]  # Get filenames from CL arguments

# Create spreadsheet
wb = openpyxl.Workbook()
sheet = wb.active

for i in range(len(files)):  # Iterate over files in file list
    col_num = i + 1  # Get column number (file number), starting at 1
    text = open(files[i])  # Open file
    lines = text.readlines()  # Get all text lines from file
    for j in range(len(lines)):  # Iterate overt text lines from file
        row_num = j + 1  # Get column number (line number), starting at 1
        # Save every line from file to cell in new row
        sheet.cell(column=col_num, row=row_num).value = lines[j]
    text.close()  # Close file

wb.save('textToSheet.xlsx')
