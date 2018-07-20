import re, os, shutil

def copyType(folder, extension):
    extensionRegex = re.compile('.*\.' + extension + '$')
    
    destination = '.\\txts'
    
    for foldername, _, filenames in os.walk(folder):
        for filename in filenames:
            if extensionRegex.search(filename):
                shutil.copy(os.path.join(foldername, filename), destination)

copyType('..', 'txt')