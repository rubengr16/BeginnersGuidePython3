# Creation of a format string using '{}' place holders
# string_name.format(value) method populates the string place holder(s) with the value(s)

my_string = '{} is {} years old'  # No index, values will follow the order in which they are provided on format

name = input('Enter your name: ')
age = input('Enter your age: ')

print(my_string.format(name, age))
print('{} has {} years'.format(name, 100))

my_string = '{1}, {2} years are equal to {0} days'  # Index determines which value matches with the place holder
#Note: index start at 0

print(my_string.format(int(age) * 365, name, age))

my_string = '{name} was born {city}, {years} ago'  # We can use names to set the values
# format() needs a pair key = value, order of the values given is not important

print(my_string.format(name = name, city = 'wherever', years = age))
print(my_string.format(name = name, years = age, city = 'wherever'))

# Width and alignment can be specified with the format method
# :value inside the curly brackets means the width
# between : and value, < means left alignment (default), ^ for centered and > for rigth

my_string = '{side:{value}25} alignment'

print(my_string.format(side = 'right', value = '>'))
print(my_string.format(side = 'centered', value = '^'))
print(my_string.format(side = 'left', value = '<'))

print('|{:^20}|'.format('20 characters width'))

# Comma as number separator and number precission format
print('{:,}'.format(123456789))
print('{:.15}'.format(123456789.012)) # Indicates precission
print('{:.5}'.format(123456789.012))
print('{:}'.format(123456789.0))