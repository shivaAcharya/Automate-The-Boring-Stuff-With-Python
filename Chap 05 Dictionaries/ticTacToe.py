
# Write your code here :-)
theBoard = {'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ',
            'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
            'bot-L' : ' ', 'bot-M' : ' ', 'bot-R' : ' '}

def printBoard(board):
    print(theBoard['top-L'] + ' | ' + theBoard['top-M'] + ' | ' + theBoard['top-R'])
    print('+++++++++')
    print(theBoard['mid-L'] + ' | ' + theBoard['mid-M'] + ' | ' + theBoard['mid-R'])
    print('+++++++++')
    print(theBoard['bot-L'] + ' | ' + theBoard['bot-M'] + ' | ' + theBoard['bot-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print(' ')
    print("It's " + turn + ' turn. Move in which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
