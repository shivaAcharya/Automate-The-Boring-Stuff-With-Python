# Program to display list of lists in a table format.

tableData = [['Shiva', 'Precious', 'Miami', 'Don', 'Neil'],
             ['Curry', 'Spaghetii', 'Salad', 'Grilled Cheese', 'Pizza'],
             ['Water', 'Dr Pepper', 'Sprite', 'Root Beer', 'Coffee']]

def printTable(inputList):
    colWidths = [0] * len(inputList)

    for i in range(len(inputList)):
        for j in range(len(inputList[i])):
            if len(inputList[i][j]) > colWidths[i]:
                colWidths[i] = len(inputList[i][j])

    for x in range(len(inputList[0])):
        for y in range(len(inputList)):
            print(inputList[y][x].rjust(colWidths[y]), end = '   ')
        print('')

printTable(tableData)


