# Write your code here :-)
dogNames = []
while True:
    print('Enter the name of dog ' + str(len(dogNames) + 1) + ' (Or enter nothing to stop.):')
    names = input()
    if names == '':
        break
    dogNames = dogNames + [names]

print('The names of your dogs are:')
for names in dogNames:
    print('   ' + names)

