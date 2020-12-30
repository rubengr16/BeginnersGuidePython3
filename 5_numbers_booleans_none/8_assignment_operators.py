# We have seen = as assingment operator, but there are several more called compound operators
# they combine together a numeric operation with the assignment operator
x = 3
print('x =', x)

x += 2  # + asignment adds the variable plus the value
print('x += 2 == x = x + 2 => x =', x)

x -= 2  # - asignment substracts the value to the variable
print('x -= 2 == x = x - 2 => x =', x)

x *= 12  # * asignment multiplies the variable by the value
print('x *= 12 == x = x * 12 => x =', x)

x /= 4  # / asignment divides the variable by the value
print('x /= 4 == x = x / 4 => x =', x)

x //= 2  # // asignment divides to floor the variable by the value
print('x //= 2 == x = x // 2=> x =', x)

x %= 1.6  # % asignment gives the modulus (reminder) of dividing the variable by the value
print('x %= 1.6 == x = x % 1.6 => x =', x)

x **= 2  # ** asignment raises the variable to the value
print('x **= 2 == x = x ** 2 => x =', x)