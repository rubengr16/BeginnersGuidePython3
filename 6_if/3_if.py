# if statement establish a condition, if it avaluates to True then some action is performed
x = int(input('Enter a number:'))

if x == 0:
    print(x, 'is not possitive neither negative')  # Indentation determines which piece of code is associated with another piece

x = int(input('Enter another number:'))

if x > 0:
    print(x, 'is possitive')  # We can indent multiple lines of code which belongs to the if
    print(x, 'squared is', x * x)

y = int(input('Enter another number:'))

if x < y:
    print(x, 'is lower than', y)
    print(x, 'multiplied by', y, 'is', x * y)

print('Good Bye')