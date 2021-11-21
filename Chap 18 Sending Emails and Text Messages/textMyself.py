#! python3
# textMyself.py - Defines the textMyself() function that texts a message
# passed to it as a string.

# Preset values:
accountSId = '####################'
authToken = '###################'
twilioNumber = '+#########'
myNumber = '+#############'

from twilio.rest import Client

def textMyself(message):
    twilioCli = Client(accountSId, authToken)
    message = twilioCli.messages.create(body = message, from_=twilioNumber, to=myNumber)