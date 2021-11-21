def collatz():
    print('Enter Number:')
    try:
        number = int(input())
        while True:
            if number <= 1:
                break
            if number %2 == 0:
                number = number/2
                print(int(number))
                continue
            if number % 2 == 1:
                number = number * 3 + 1
                print(int(number))
                continue
    except ValueError:
        print('This is not a number. Please enter a valid number:')
        collatz()
collatz()

pip install PyDictionary
