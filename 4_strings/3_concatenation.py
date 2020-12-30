# String concatenation is possible through '+' operator
my_string = 'Good'
my_string2 = "Day"
print(my_string + my_string2)  # Notice it has no effect the quote type

print('Hello ' + 'World')  # Concatenate directly on print function

new_string = my_string + my_string2  # Concatenate to form a new string and save it in a variable
print(new_string)

# Concatenate them with a space as separator
new_string = my_string + ' ' + my_string2  # string concatenation
print(new_string)