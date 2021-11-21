# Write your code here :-)
import random

a = random.randint(1, 30)
print("I am thinking of a number between 1 and 30.")
print("Take a guess.")

"""while True:
    guessNumber = input()
    if int(guessNumber) > a:
        print ('Your guess is too high.')
        continue
    if int(guessNumber) < a:
        print ('Your guess is too low.')
        continue
    else:
        break

"""

for i in range(10000):

    guessNumber = input()
    if int(guessNumber) > 30 or int(guessNumber) < 1:
        print(
            ""
            + guessNumber
            + " is not between 1 and 30. You STUPID!! You Lost your ONE ATTEMPT."
        )
    if int(guessNumber) > a and int(guessNumber) < 30:
        print("Your guess is too high.")
        i = i + 1
    if int(guessNumber) < a and int(guessNumber) > 1:
        print("Your guess is too low.")
        i = i + 1
    if int(guessNumber) == a:
        i = i + 1
        print("Good job! You guessed my number in " + str(i) + " response(s).")
