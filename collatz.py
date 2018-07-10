#Guess a random number game

def collatz(number):
    if number%2 == 0:
        value = number // 2
    else:
        value = (3*number)+1
    print(value)
    return value

print('Enter number:')
while True:
    try:
        number = int(input())
    except:
        print('Input must be an integer.')
while number != 1:
    number = collatz(number)