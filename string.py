# Chapter 4. Python Strings

phrase = 'Python, C, Java, Fortran, are programming languages'

# Input of 2 strings
my_string = input('Enter a string: ')
print(my_string)
my_string2 = input('Enter a second string: ')
print(my_string2)

# concatenate them with a space as separator
new_string = my_string + ' ' + my_string2  # String concatenation
print('String concatenation: ', new_string)

# Length of my_string, my_string2 and new_string
print('my_string length: ', len(my_string))
print('my_string2 length: ', len(my_string2))
print('new_string length: ', len(new_string))

# String repetition
print('#' * 40)

# Access characters through their index
print('Source Phrase', phrase)
print('phrase[4]: ', phrase[4], 'phrase[7]: ', phrase[7])

# Access substring
print('phrase[:4]: ', phrase[:4])  # Substring form index 0 to 3, last index is excluded
print('phrase[12:]: ', phrase[12:])  # From index 12 to the end
print('phrase[7:12]: ', phrase[7:12])

print('#' * 40)

# Split a string
print('Source Phrase', phrase)
print('Split using ",": ', phrase.split(','))
print('Split using "a": ', phrase.split('a'))

print('#' * 40)

# Count how many times are repeated a substring
print('Source Phrase', phrase)
print('", " is repeated', phrase.count(', '), 'time(s)')

# Replace commas with spaces
print(phrase)
print(phrase.replace(',', ' '))

# new_string to upper case
print(new_string.upper())

# new_string contains 'hello'?:  Affirmative: 1st letter index || Negative: -1
print('Does "SQL" appear on phrase?: ', phrase.upper().find('SQL'))
print('Does "Java" appear on phrase?: ', phrase.upper().find('Java'.upper()))
