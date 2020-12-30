# Adding: +, substracting: - and multiplying: * between complex returns a complex number
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

# Division: / returns a float, although the numbers divide each other exactly
print('x / y =', x / y)
print('x / y type:', type(x / y))

print('(x - 1) / y =', (x - 1) / y)
print('(x - 1) / y type:', type((x - 1) / y))

# Integer division: // is not possible in complex numbers
# Modulus: % is not possible in complex

# Power: ** raises an int by a given power
print('x ** y =', x ** y)
print('x ** y type:', type(x ** y))

# More complex operations can be made using math module