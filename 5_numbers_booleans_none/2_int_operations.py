# Adding: +, substracting: - and multiplying: * between int produces an int result
x = 13
y = 2

print('x =', x, 'y =', y)
print('x type:', type(x), 'x type:', type(y))

print('x + y =', x + y)
print('x + y type:', type(x + y))

print('x - y =', x - y)
print('x - y type:', type(x - y))

print('x * y =', x * y)
print('x * y type:', type(x * y))

# Division: / returns a float, although the numbers divide each other exactly
# it defaults a floating point number as python does not know which result will be given
print('x / y =', x / y)
print('x / y type:', type(x / y))

print('(x - 1) / y =', (x - 1) / y)
print('(x - 1) / y type:', type((x - 1) / y))

# integer division: // returns an int, ignoring the fractional part
print('x // y = ', x // y)
print('x // y type:', type(x // y))

# modulus: % returns the remainder of a division operation
print('x % y =', x % y)
print('x % y type:', type(x % y))

# power: ** raises an int by a given power
print('x ** y =', x ** y)
print('x ** y type:', type(x ** y))

# the same integer operations are possible with negative numbers
x = -1 * x

print('x // y = ', x // y)  # note: integer division rounds towards minus infinity, the smallest number possible
print('x // y type:', type(x // y))