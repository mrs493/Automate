from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

try:
    htmlElem = browser.find_element_by_tag_name('html')
    while True:
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)
        htmlElem.send_keys(Keys.RIGHT)
except Exception as err:
    print(err)