import os, re

print('Enter path to directory to be seached:')
path = input()

while not os.path.isdir(path):
    print('Not a valid directory.\nPlease enter a directory:')
    path = str(input())

print('\nPlease enter the text to be searched for (remember to escape special characters):')
regex = re.compile(input(), re.I)

for file in os.listdir(path):
    if file[-4:] == '.txt':
        with open(os.path.join(path, file)) as txtFile:
            lines = txtFile.readlines() 
        for line in range(len(lines)):
            if regex.search(lines[line]):
                print('%s: line %i' % (file, line+1))

#get path from user
    #check is valid

#get regex from user

#get files from directory
    #open each .txt
    #search each line for match
    #print matching file names and line numbers
    
