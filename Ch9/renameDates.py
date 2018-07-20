#! python2
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

dateRegex = re.compile(r'''
                       ^(.*?)       #leading text
                       (\d{1,2})    #month
                       -            #connector
                       (\d{1,2})    #days
                       -            #connector
                       ((\d\d){1,2})  #year
                       (.*?)$       #trailing text
                       ''', re.VERBOSE)

for filename in os.listdir('.'):
    mo = dateRegex.search(filename)
    if mo:
        newFilename = ''
        if newFilename:
            newFilename += mo.group(1)
        newFilename = mo.group(3) + '-' + mo.group(2) + '-' + mo.group(4) + mo.group(6)
        print(newFilename)
        print('Renaming file "%s" to "%s"' % (filename, newFilename))
        #shutil.move(filename, newFilename)     #uncomment to change filename
        