import re


def stripRegex(text, char='\s'):
    strip = re.compile(fr'(^{char}*|{char}*$)')
    return strip.sub('', text)


text = 'feafrzrfff'
print(f'Before stripping: {text}')

print(f'After stripping: {stripRegex(text, "f")}')