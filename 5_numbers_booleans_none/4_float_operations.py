# adding: +, substracting: - and multiplying: * are also possible between floats, of course, returning floats
x = 13.95
y = 2.15

print('x =', x, 'y =', y)
print('x type:', type(x), 'x type:', type(y))

print('x + y =', x + y)
print('x + y type:', type(x + y))

print('x - y =', x - y)
print('x - y type:', type(x - y))

print('x * y =', x * y)
print('x * y type:', type(x * y))

# division: /
print('x / y =', x / y)
print('x / y type:', type(x / y))

print('(x - 1) / y =', (x - 1) / y)
print('(x - 1) / y type:', type((x - 1) / y))

# integer division: //
print('x // y = ', x // y)
print('x // y type:', type(x // y))

# modulus: %
print('x % y =', x % y)
print('x % y type:', type(x % y))

# power: **
print('x ** y =', x ** y)
print('x ** y type:', type(x ** y))

# the same float operations are possible with negative numbers
x = -1 * x

print('x // y =', x // y)
print('x // y type:', type(x // y))

# once we mix up int and float, we will have a float result
# it will happens every time we have a float on one side of the operation
x = 3
print('x =', x, 'x type:',  type(x))
x = 3 * 0.1  # we will get an aproximation: 0.30000000000000004 due to the IEEE 154 double-precission representation
print('x =', x, 'x type:',  type(x))

# more precise aproximation is possible using the decimal module (or library) which provides de Decimal class
from decimal import Decimal
x = Decimal(3 * 0.1)
print('x =', x, 'x type:',  type(x))