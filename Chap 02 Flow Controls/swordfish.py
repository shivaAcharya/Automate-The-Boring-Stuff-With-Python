while True:
    print('What is your name?')
    name = input()
    if name != 'Joe':
        continue
    break
password = ''
while True:
    print('Joe, what is the password? (It is a fish.)')
    password = input()
    if password != 'swordfish':
        continue
    break
print('Access Granted!')
