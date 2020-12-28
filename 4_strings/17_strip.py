# string_name.strip(substring_of_characters) method 
# returns a string copy removing the leading and trailing characters specified on substring_of_characters
phrase = 'Python, C, Java, Fortran, are programming languages'

print(phrase)
print(phrase.strip('Psy'))
phrase = ' ' + phrase + ' '
print(phrase)
print(phrase.strip(' Pse'))
phrase = phrase.strip(' ')  # phrase to initial state