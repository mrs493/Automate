import re

with open('madLib.txt') as madLibFile:
    madLib = madLibFile.read()

words = madLib.split()

regex = [re.compile(r'^([(-])*(ADJECTIVE)([.!?)-])*'), re.compile(r'^([(-])*(NOUN)([.!?)-])*'), re.compile(r'^([(-])*(ADVERB)([.!?)-])*'), re.compile(r'^([(-])*(VERB)([.!?)-])*')]

for i in range(len(words)):
    for reg in regex:
        mo = reg.search(words[i])
        if mo:
            print('enter a %s:' % mo[2].lower())
            words[i] = input()
            if mo[1]: words[i] = mo[1] + words[i]
            if mo[3]: words[i] += mo[3]
    '''
    if words[i] in ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']:
        print('enter a %s:' % words[i].lower())
        words[i] = input()
    '''
madLibbed = ' '.join(words)

print(madLibbed)

with open('madLibbed.txt', 'w') as madLibbedFile:
    madLibbedFile.write(madLibbed)