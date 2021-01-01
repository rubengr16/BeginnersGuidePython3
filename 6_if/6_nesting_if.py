# It is possible to nest one if statement inside another, 
# it consists of locating one if statement inside another if statement,
# it can be used to refine the conditional behaviour
# Note: keep in mind the importance of indentation
temperature = int(input('Enter the outside temperature: '))
snowing = True

if temperature < 0:
    print('It is freezing')
    if snowing:  # Nested if
        print('It is snowing')
    print('Be careful with the ice')  # It will be printed if the outer if is executed
else:
    print('There are suposed safe meteorological conditions')
print('Bye')  # It will be printed always