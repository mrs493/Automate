import re

def strengthTest(password):
    upper = re.compile(r'[A-Z]')
    lower = re.compile(r'[a-z]')
    digit = re.compile(r'\d')
    if len(password)<8:
        print(0)
        return False
    if not upper.search(password):
        print(1)
        return False
    if not lower.search(password):
        print(2)
        return False
    if not digit.search(password):
        print(3)
        return False
    return True


password = 'Passw0rd'
print(strengthTest(password))    