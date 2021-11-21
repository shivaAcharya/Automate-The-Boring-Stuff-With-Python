# Program to check if a given text is a valid phone number.

def isPhoneNumber(text):
    #Check if length of given text is 12.
    if len(text) != 12:
        return False

    #Check first 3 values of text string are decimals.
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    #Check if there is - in 4th and 8th place of given text.
    if text[3] != '-' or text[7] != '-':
        return False

    #Check if mid 3 values are numbers.
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    #Check if last 4 values are numbers.
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True

message = 'Call me at 505-492-8001. 424-206-8316 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone Number found. ' + chunk)
print('Done!')
