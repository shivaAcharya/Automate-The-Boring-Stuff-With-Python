# Program To Keep An Idiot Busy For Hours

import pyinputplus as pyip

while True:
    prompt = 'Do you want to know how to keep an idiot busy for hours?\n'

    response = pyip.inputYesNo(prompt)

    if response == 'no':
        break

print('Thank you for your time.')
