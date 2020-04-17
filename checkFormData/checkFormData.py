#!usr/bin/env python3
# getFormData.py - Downloads emails from google sheets
# file with form answers.

import ezsheets

sheet_url = '1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg'

ss = ezsheets.Spreadsheet(sheet_url)
sheet = ss[0]  # Get first worksheet
rows = sheet.getRows()
for i in range(1, len(rows)):
    if (rows[i][0] != '') and (
                               int(rows[i][0])
                               * int(rows[i][1])
                               != int(rows[i][2])
                               ):
        print('Row with incorrect number: ' + str(i + 1))
        print(f'Its now: {rows[i][2]}')
        print(f'It should be: {int(rows[i][0]) * int(rows[i][1])}')
