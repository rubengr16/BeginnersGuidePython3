# string.isupper() method tells us if a string is upper case, string.islower() if is lower and both return a boolean
# string.upper() method changes the string case to upper, string.lower() to lower
# string.swapcase() method shap the existing cases, from upper to lower and viceversa
phrase = 'Python, C, Java, Fortran, are programming languages'

print('phrase is upper?: ', phrase.isupper())
print('phrase to upper: ', phrase.upper())
print('phrase to lower: ', phrase.islower())
print('phrase is lower?: ', phrase.lower())
print('phrase swapping case: ', phrase.swapcase())