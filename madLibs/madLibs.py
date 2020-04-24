#! python3

import re

file = open('baseText.txt', 'r')
newfile = open('madLibs.txt', 'w')

content = file.read()

wordRegex = re.compile(r'(adjective|noun|verb)', re.I)

divide = content.split()
new_content = []

for item in divide:
    searchReg = wordRegex.search(item)
    if searchReg is not None:
        answer = input(f'Enter {searchReg.group().lower()}: ')
        item = wordRegex.sub(answer, item)
    new_content.append(item)

new_content = ' '.join(new_content)
print(new_content)
newfile.write(new_content)
file.close()
newfile.close()
