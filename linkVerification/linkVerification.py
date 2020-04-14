#!usr/bin/env python3
# linkVerification.py - Program downloading all links from website
# and checking their statuscodes.

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org'

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

urls = []

for link in soup.find_all('a'):
    href = link.get('href')
    if '//' not in href:
        href = url + href
    elif href[:2] == '//':
        href = 'https:' + href
    urls.append(href)

for url in urls:
    try:
        new_res = requests.get(url)
        if new_res.status_code != 200:
            print(f'Status code: {new_res.status_code} for: {url}')
    except requests.exceptions.InvalidURL:
        print(f'This is not valid URL: {url}. Skipping..')
        continue
