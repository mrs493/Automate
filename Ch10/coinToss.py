import random

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads

assert toss in (0, 1), 'random number not 0 or 1'

if toss == 0:
    toss = 'tails'
elif toss == 1:
    toss = 'heads'
 
assert toss in ('heads', 'tails'), 'toss not coin face'
   
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss again! Enter heads or tails:')
        guess = input()
    if toss == guess:
        print('You got it!')
    else:
x        print('Nope. You are really bad at this game.')