#Program To Make Your Own Sandwich

import pyinputplus as pyip

Sandwich = []

#Select Bread

print('Type of bread: \n')
response = pyip.inputMenu(['White', 'Wheat', 'Sourdough'], numbered = True)
Sandwich.append(response)

#Select Protein

print('\nType of protein: \n')
response = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered = True)
Sandwich.append(response)

#Need Cheese?

print('\nWant to add cheese?\n')
response = pyip.inputYesNo()
Sandwich.append('Cheese - ' + response)

if response == 'yes':
    #Select Cheese
    print('\nType of cheese" \n')
    response = pyip.inputMenu(['Chedder', 'Swiss', 'American', 'Mozzarella'], numbered = True)
    Sandwich.append(response)

#Need Mayo?

print('\nWant to add mayo?\n')
response = pyip.inputYesNo()
Sandwich.append('Mayo - ' + response)

#Need Lettuce?

print('\nWant to add lettuce?\n')
response = pyip.inputYesNo()
Sandwich.append('Lettuce - ' + response)

#Need Tomato?

print('\nWant to add tomato?\n')
response = pyip.inputYesNo()
Sandwich.append('Tomato - ' + response)

#How many sandwiches?

print('\nHow many sandwiches?\n')
response = pyip.inputInt(min = 1)
Sandwich.append('Qty - ' + str(response))

print(Sandwich)
