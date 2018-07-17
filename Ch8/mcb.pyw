#! python2
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage:  py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#         py.exe mcb.pyw delete <keyword> - Delete keyword.
#         py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#         py.exe mcb.pyw delete - Delete all keywords.
#         py.exe mcb.pyw list - Loads all keywords to clipboard.

import pyperclip, shelve, sys

shelfFile = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        shelfFile[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete' and sys.argv[2] in shelfFile:
        del shelfFile[sys.argv[2]]

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy('\n'.join(shelfFile.keys()))
    elif sys.argv[1].lower() == 'delete':
        for key in shelfFile:
            del shelfFile[key]
    elif sys.argv[1] in shelfFile:
        pyperclip.copy(str(shelfFile[sys.argv[1]]))

shelfFile.close()