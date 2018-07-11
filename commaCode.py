def read(lst):
    for i in range(len(lst)-2):
        print(lst[i], end=', ')
    print(lst[-2] + ' and ' + lst[-1])

spam = ['apples', 'bananas', 'tofu', 'cats']

read(spam)