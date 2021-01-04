# The while loop repeats a block of code while a test condition is True,
# it is used when the number of iterations (repetitions) is unknown,
# the test of the condition is made before each iteration,
# it has the form: while test_condition_is_true:
#                       block_of_code
# Note: indentation is important
print('Enter values to be powered by themselves, 0 to stop')
num = int(input('Enter a value: '))  # num must be initialised before the while as it is part of the test condition

while(num != 0):  # num != 0 is the test condiition
    print(num, 'squared is', num * num)
    num = int(input('Enter a value: '))

print('Done')  # Statement out of the while