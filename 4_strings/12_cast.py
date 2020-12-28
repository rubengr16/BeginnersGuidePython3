# str(variable_or_value) function converts variable_or_value to string
phrase = 'Python, C, Java, Fortran, are programming languages'
x = 3.14

# phrase = phrase + 21 + True + x  # gives an error, so cast is needed...
phrase = phrase + str(21) + str(True) + str (x)
print(phrase)
phrase = phrase[:phrase.find('21')]  # restore phrase's initial value
print(phrase)