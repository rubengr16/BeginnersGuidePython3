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