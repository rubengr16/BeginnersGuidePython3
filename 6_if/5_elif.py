# Follows the if part and comes before any (optional) eles part,
# has the format: elif condition_evaluating_to_boolean:
#                     statement 
age = int(input('Enter your age: '))

if age < 0:
    print('You must enter a real age')
elif age < 4:
    print('You are almost a baby')
elif age < 12:
    print('You are a child')
elif age < 18:
    print('You are a teenager')
elif age < 65:
    print('You are an adult')
else:  # optional
    print('Enjoy yourself for the rest of your life')