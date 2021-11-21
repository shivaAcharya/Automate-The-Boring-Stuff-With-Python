# Write your code here :-)
import random


def getAnswer(ansNumber):
    if ansNumber == 1:
        return "This is very poor score!"
    elif ansNumber == 2:
        return "This is poor score!"
    elif ansNumber == 3:
        return "This is below average score!"
    elif ansNumber == 4:
        return "This is average score!"
    elif ansNumber == 5:
        return "This is average score!"
    elif ansNumber == 6:
        return "This is good score!"
    elif ansNumber == 7:
        return "This is very good score!"
    elif ansNumber == 8:
        return "This is excellent score!"
    elif ansNumber == 9:
        return "This is outstanding score!"


r = random.randint(1, 9)
print(r)
print(getAnswer(r))
