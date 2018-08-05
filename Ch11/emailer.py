import sys, pyperclip, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#take command line argument of email and optional message
'''
if len(sys.argv) < 2:
    raise Exception('please enter an email adress')

address = sys.argv[1]
    
if len(sys.argv) > 2:
    message = ' '.join(sys.argv[2:])

else:
    message = pyperclip.paste()

print(address)
print(message)
'''
#log into emails

with open('email.txt', 'r') as details:
    email = details.readline()[:-1]
    password = details.readline()

browser = webdriver.Firefox()
browser.get('https://accounts.google.com/')

emailElem = browser.find_element_by_name('identifier')
emailElem.send_keys(email)
emailElem.send_keys(Keys.ENTER)
time.sleep(5)
pwElem = browser.find_element_by_name('password')
pwElem.send_keys(password)
pwElem.send_keys(Keys.ENTER)

time.sleep(5)

browser.get('https://mail.google.com/mail/')

time.sleep(10)

#send a message to the given email and message, or clipboard if not given
msgElem = browser.find_element_by_class_name('T-I J-J5-Ji T-I-KE L3')
msgElem.click()
