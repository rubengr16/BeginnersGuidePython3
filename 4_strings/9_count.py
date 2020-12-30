# Using the string_names.count(substring) method we can count how many times is repeated a substring
phrase = 'Python, C, Java, Fortran, are programming languages'

print('Source Phrase', phrase)
print('", " is repeated', phrase.count(', '), 'time(s)')
print('"$" is repeated', phrase.count('$'), 'time(s)')
print('"an" is repeated', phrase.count('an'), 'time(s)')