# Write your code here :-)
import random

messages = ['Yes absolutely!',
            'Definitely not',
            'Its hazy, try asking again!',
            'Maybe!',
            'Concentrate and ask again',
            'My reply is no',
            'Very doubtful',
            'Outlook not so good']

print(messages[random.randint(0, len(messages) -1)])
