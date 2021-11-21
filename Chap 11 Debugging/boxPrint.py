#Program to Raise and Handle Exceptions

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception ('The symbol should be one charcacter long.')

    if width <= 2:
        raise Exception('The width should be greater than 2')

    if height <= 2:
        raise Exception('The height should be greater than 2')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 3, 3), ('#', 20, 8), ('0', 3, 1), ('##', 5, 6)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An Exception found: ' + str(err))


