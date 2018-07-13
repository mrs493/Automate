#! python2
#! pw.py - An insecure password locker programe

import sys
import pyperclip

PASSWORDS = {'email':'passw0rd',
             'blog':'s3cr3t',
             'luggage':'73856'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')

else:
    print('There is no account named ' + account)

