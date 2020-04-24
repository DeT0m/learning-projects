#!usr/bin/env python3

import re


def isValidDate(day, month, year):
    message = 'The date is valid'

    if int(year) % 100 == 0 and int(year) % 400 != 0 and int(day) > 28 and int(month) == 2:
        message = 'This is not valid leap year.'
    elif int(year) % 4 != 0 and int(day) > 28 and int(month) == 2:
        message = 'This is not valid leap year.'

    if int(month) > 12:
        message = 'This is not valid month number.'

    if ((int(month) in [4, 6, 9, 11] and int(day) > 30) or
            (int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) > 31)):
        message = 'This is not valid day of the month.'

    return message


text = '31/12/2013'

dateRegex = re.compile(r'''(
    ([0-3][0-9])    #day number 01-31
    \/  #separator
    ((0|1)[0-9])    #month number 01-12
    \/  #separator
    ((1|2)[0-9]{3}) #year number 1000-2999
    )''', re.VERBOSE)


for groups in dateRegex.findall(text):
    day = groups[1]
    month = groups[2]
    year = groups[4]


print(f'{day}\n{month}\n{year}')

print(isValidDate(day, month, year))
