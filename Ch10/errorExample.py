import traceback

def spam():
    bacon()

def bacon():
    raise Exception('This is an error')

try:
    spam()
except:
    with open('error.txt', 'w') as errorFile:
        errorFile.write(traceback.format_exc())
    print('Traceback info written to error.txt')