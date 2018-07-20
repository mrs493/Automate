#! python2
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

#find current number and incriment
#make zip
#save files to zip

import re, os, zipfile

def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    
    folder = os.path.abspath(folder)
    
    lenPath = len(folder)
    
    foldernameRegex = re.compile('^' + os.path.basename(folder) + '_backup_(\d)+.zip$')
    
    number = 1
    
    for filename in os.listdir(folder):
        mo = foldernameRegex.search(filename)
        if mo:
            if int(mo.group(1)) >= number:
                number = int(mo.group(1)) + 1
    
    backupName = os.path.basename(folder) + '_backup_' + str(number) + '.zip'
    
    print('creating %s...' % backupName)
    
    backupZip = zipfile.ZipFile(backupName, 'w')
    
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        for filename in filenames:
            if not foldernameRegex.search(filename):
                backupZip.write(os.path.join(foldername, filename), os.path.join(foldername[lenPath:], filename))
    print('Backup complete')
    
    backupZip.close()
            
backupToZip('.')