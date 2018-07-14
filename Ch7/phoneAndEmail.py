#! python2
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''
                        (\d{3}|\(\d{3}\))?              #area code
                        (\s|-|\.)?                      #separator
                        (\d{3})                         #first 3 digits
                        (\s|-|\.)                       #separator
                        (\d{4})                         #last 4 digits
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?    #extension
                        ''', re.VERBOSE)

emailRegex = re.compile(r'''
                        [a-zA-Z0-9._%+-]+               #username
                        @                               #@ symbol
                        [a-zA-Z0-9.-]+                  #domain name
                        \.[a-zA-Z0-9.]{2,}              #top-level domain
                        ''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
    no = '-'.join([groups[0], groups[2], groups[4]])
    if groups[7] != '':
        no += ' x ' + groups[7]
    matches.append(no)

for email in emailRegex.findall(text):
    matches.append(email)

matches = '\n'.join(matches)

if matches:
    pyperclip.copy(matches)
    print('Copied to clipboard:')
    print(matches)

else:
    print('No phone numbers or emails found in text')
    