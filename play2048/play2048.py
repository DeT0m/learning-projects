#!usr/bin/env python3
# play2048.py - play 2048 game with automated script

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://play2048.co/')  # Open game site in browser


def elem():
    return browser.find_elements_by_class_name('game-over')


while len(elem()) == 0:
    action = ActionChains(browser)
    action.send_keys(
        Keys.ARROW_UP,
        Keys.ARROW_RIGHT,
        Keys.ARROW_DOWN,
        Keys.ARROW_LEFT
        )
    action.perform()
    elem()

score_elem = browser.find_elements_by_class_name('score-container')
print(f'Game over!\nYour score is: {score_elem[0].text}.')
