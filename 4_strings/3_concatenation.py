# string concatenation is possible through '+' operator
my_string = 'Good'
my_string2 = "Day"
print(my_string + my_string2)  # notice it has no effect the quote type

print('Hello ' + 'World')  # concatenate directly on print function

new_string = my_string + my_string2  # concatenate to form a new string and save it in a variable
print(new_string)

# concatenate them with a space as separator
new_string = my_string + ' ' + my_string2  # String concatenation
print(new_string)