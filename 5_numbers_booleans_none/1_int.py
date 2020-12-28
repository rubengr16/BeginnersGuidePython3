# integral numbers are represented by int type indepently from their size
integer = 1
print(integer)
print('x type:', type(integer))

x = 1111111111111111111111222222222233333333333333333333333333333334444444444444444444444555555555555
print(integer)
print('x type:', type(integer))

# int() function can be used to cast to int
integer = int('98')
print(integer)
print(type(integer))


integer = 1.65
print('x type:', type(integer), integer)
print(int(integer))

# input() function always returns a string, we can also cast it
integer = int(input("Enter a whole number: "))
print(integer)