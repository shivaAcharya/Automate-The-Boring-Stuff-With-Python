# Progam to guess coin flip

import random
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 for heads and 1 for tails
if toss == 0:
    toss = 'heads'
else:
    toss = 'tails'

if toss == guess:
    print('You guessed it right!')

else:
    print('You guessed wrong, try it again!')
    guess = input()
    if toss == guess:
        print('You got it.')
    else:
        print('You are really bad at this game.')
