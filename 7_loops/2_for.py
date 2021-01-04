# The for loop is used when we know how many times we need to iterate, 
# we step a variable through a series of values until a given test is met,
# to do this, we will use the range function to generate a range of values to be used as the sequence in the loop
# it is also possible to loop over data structures,
# the for loop has the following form: for variable_name  in range (...):
#                                           block_of_code
print('Numbers from 0 to 10:')

for i in range(0, 10):  # i variable does not need initialization, the range is range(initial_value, end_value),
# the end_value is excluded 
    print(i, ' ', end = '')  # print function prints a new line in each call, end = ' ' avoids it and allows us to
# print in the same line

print()
print('Done')