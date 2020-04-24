import re

passwordSymbols = re.compile(r'[\d\w\.\@\$\%\^\&\*\_\-\=\+\`\|\~\!\"\'\;\:\,\<\>\/\\\#]{8,}')
passwordLettersLow = re.compile(r'.*[a-z]+.*')
passwordLettersHigh = re.compile(r'.*[A-Z]+.*')
passwordNumbers = re.compile(r'.*[0-9]+.*')

password = 'a3bc#dDfe^'


def isValidPassword(text):
    length = passwordSymbols.search(text)
    letters_low = passwordLettersLow.search(text)
    letters_high = passwordLettersHigh.search(text)
    numbers = passwordNumbers.search(text)
    if (length is not None and letters_low is not None and
            letters_high is not None and numbers is not None):
        print(f'Your password is valid. Password: {text}')
    else:
        print(f'Your password is not valid. Password: {text}')


isValidPassword(password)
