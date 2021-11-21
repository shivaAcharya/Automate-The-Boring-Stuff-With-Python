# Write your code here :-)

'''         Ending a Program Early with the sys.exit() Function

The last flow control concept to cover is how to terminate the program.
Programs always terminate if the program execution reaches the bottom
of the instructions. However, you can cause the program to terminate, or
exit, before the last instruction by calling the sys.exit() function. Since this
function is in the sys module, you have to import sys before your program
can use it.'''

import sys

while True:
    print('Enter exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print ('You entered ' + response + '.')

''' Run this program in IDLE. This program has an infinite loop with no
break statement inside. The only way this program will end is if the execution
reaches the sys.exit() call. When response is equal to exit, the line containing
the sys.exit() call is executed. Since the response variable is set by
the input() function, the user must enter exit in order to stop the program.'''

