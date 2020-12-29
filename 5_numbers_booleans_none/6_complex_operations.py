# adding: +, substracting: - and multiplying: * between complex returns a complex number
x = 13 + 5j
y = 2 + 3j

print('x =', x, 'y =', y)
print('x type:', type(x), 'x type:', type(y))

print('x + y =', x + y)
print('x + y type:', type(x + y))

print('x - y =', x - y)
print('x - y type:', type(x - y))

print('x * y =', x * y)
print('x * y type:', type(x * y))

# division: / returns a float, although the numbers divide each other exactly
# it defaults a floating point number as python does not know which result will be given
print('x / y =', x / y)
print('x / y type:', type(x / y))

print('(x - 1) / y =', (x - 1) / y)
print('(x - 1) / y type:', type((x - 1) / y))

# integer division: // is not possible in complex numbers
# modulus: % is not possible in complex

# power: ** raises an int by a given power
print('x ** y =', x ** y)
print('x ** y type:', type(x ** y))

# more complex operations can be made using math module