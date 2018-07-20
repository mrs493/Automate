#ToDo

import os, re, shutil

folder = r'C:\Users\Matt\Desktop\Code\Automate\Ch9\Quizes'

filenames = os.listdir(folder)

prefix = 'quiz'

numberRegex = re.compile(prefix + '(\d+)(.*)')

fileNumbers = {}

length = 0

for filename in filenames:
    mo = numberRegex.search(filename)
    if mo:
        fileNumbers[mo.group(1)] = mo.group()
        if len(mo.group(1))>length:
            length = len(mo.group(1))

numbers = list(fileNumbers.keys())

high = max([int(x) for x in numbers])

for index in range(1, high + 1):
    if numbers[index] == index:
        continue
    shutil.move()
    
'''
newIndex = []
shift = 0

for index in range(1, high + 1):
    if index not in intNum:
        shift+=1
    newIndex.append(index - shift)
'''