#! python3

import re
from pathlib import Path

user_input = input('Write your regex here: ')

user_regex = re.compile(user_input)

p = Path.cwd()

for file in p.glob('*.txt'):
    file_open = open(file)
    lines = file_open.readlines()
    for line in lines:
        if user_regex.search(line) is not None:
            print(f'Found in {file}\nContent: {line}')
    file_open.close()
