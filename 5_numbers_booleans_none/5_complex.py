# Complex numbers are defined by: real_part + imaginary_part
# this imaginary part is: real_coefficient * j, j is the imaginary part of the number i engineering notation
# the real part is a real number added to the imaginary number
# finally, a complex number is: real_number + (real_coefficient * j)

complex_1 = 1 + 5j
print(complex_1)
print('complex_1 type:', type(complex_1))
print('complex_1 real part:', complex_1.real)  # complex_name.real returns the real part of the complex number
print('complex_1 imaginary part:', complex_1.imag)  # complex_name.imaginary gives imaginary_part's real_coefficient

# It is possible to convert another number or string into a complex number
# from int
x = 2
print('x =', x, 'x type:', type(x))

x = complex(x)
print('x =', x, 'x type:', type(x))

# from float
x = 2.25
print('x =', x, 'x type:', type(x))

x = complex(x)
print('x =', x, 'x type:', type(x))

# from string
x = '3'
print('x =', x, 'x type:', type(x))

x = complex(x)
print('x =', x, 'x type:', type(x))