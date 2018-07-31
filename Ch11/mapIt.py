#! python2
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
import pyperclip, sys, webbrowser

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

else:
    address = pyperclip.paste()

print(address)

webbrowser.open('http://www.google.com/maps/place/' + address)