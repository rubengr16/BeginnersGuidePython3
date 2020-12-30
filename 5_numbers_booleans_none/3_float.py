# Real numbers are represented by float type with the IEEE 154 double-precission binary floating point number format
my_float = 1.65
print(my_float)
print(type(my_float))

# int() function can be used to cast to int
my_float = float('109.654')
print(my_float)
print(type(my_float))

my_float = '1090.6'
print(my_float)
print(type(my_float))

my_float = 125
print(float(my_float))
print(type(my_float))

# input() function always returns a string, we can also cast it
my_float = float(input("Enter a decimal number: "))
print(my_float)