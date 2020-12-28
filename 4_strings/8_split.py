# string.split(character) splits a string using the character given
# note: we call the split METHOD with the string_name.split
phrase = 'Python, C, Java, Fortran, are programming languages'

print('Source Phrase', phrase)
print('Split using ",": ', phrase.split(','))  # uses ',' as separator and delete where it appears
print('Split using "a": ', phrase.split('a'))