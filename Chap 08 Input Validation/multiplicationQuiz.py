# Program To Ask 10 Multiplication Problems.

import pyinputplus as pyip
import random, time, re

#Ten questions each

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):

    #Select random numbers between 1 to 10 for multiplication
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    #Pose multiplication question.
    prompt = '#%s : %s x %s = ' % (questionNumber+1, num1, num2)

    try:
        pyip.inputStr(prompt, allowRegexes = ['^%s$' % (num1*num2)], blockRegexes = [('.*', 'Incorrect!!')], timeout = 20, limit = 3,)
    except pyip.TimeoutException:
        print('Time Out!')
    except pyip.RetryLimitException:
        print('Out of Tries!')

    else:
        correctAnswers += 1
        print('Correct Answer!')
    time.sleep(1)
print('%s / %s' %(correctAnswers, numberOfQuestions))
