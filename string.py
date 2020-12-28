# Chapter 4. Python Strings

phrase = 'Python, C, Java, Fortran, are programming languages'

# Count how many times are repeated a substring
print('Source Phrase', phrase)
print('", " is repeated', phrase.count(', '), 'time(s)')

# Replace commas with spaces
print(phrase)
print(phrase.replace(',', ' '))

# new_string contains 'hello'?:  Affirmative: 1st letter index || Negative: -1
print('Does "SQL" appear on phrase?: ', phrase.upper().find('SQL'))
print('Does "Java" appear on phrase?: ', phrase.upper().find('Java'.upper()))

# converting to string
# phrase = phrase + 21  # gives an error, so cast is needed...
phrase = phrase + str(21)
print(phrase)
phrase = phrase[:phrase.find('21')]  # restore phrase's initial value

# string comparison
jon = 'jon'
ygritte = 'ygritte'
print(jon == jon)
print(jon == ygritte)
print(jon != ygritte)

print('#' * 40)

# starts and ends with
print('jon starts with "j": ', jon.startswith('j'))
print('jon starts with "y": ', jon.startswith('y'))
print('ygritte ends with "j": ',ygritte.endswith('j'))
print('ygritte ends with "e": ', ygritte.endswith('e'))

print('#' * 40)

# upper case and lower
print('phrase is upper?: ', phrase.isupper())
print('phrase to upper: ', phrase.upper())
print('phrase to lower: ', phrase.islower())
print('phrase is lower?: ', phrase.lower())
print('phrase swapping case: ', phrase.swapcase())

# title and alpha
print('phrase is title?: ', phrase.istitle())
print('phrase to title: ', phrase.title())
print('phrase is alpha?: ', phrase.isalpha())

# string leading, trailing characters
print(phrase)
print(phrase.strip('Psy'))
phrase = ' ' + phrase + ' '
print(phrase)
print(phrase.strip(' Pse'))
phrase = phrase.strip(' ')  # phrase to initial state