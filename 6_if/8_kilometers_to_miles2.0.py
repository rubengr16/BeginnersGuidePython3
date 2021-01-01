# Take input from the user in a given distance in kilometres, 
# new: make sure it is a possitive distance and the input is a number, if not, do nothing,
# otherwise convert the value returned from a string to float
# convert the value into miles (dividen the kilometers by 0.6214)
# print out a message saying to the user what the kilometres are in miles  
kilometres_to_miles = 0.6214
kilometres = input('Enter a distance in kilometres: ')

if kilometres.isnumeric() or kilometres.replace('.', '').isdigit() or kilometres.replace(',', '').isdigit(): 
    # string_name.isnumeric() checks for a string with only digits
    # string_name.replace('.', '').isdigit or string_name(',', '').isdigit() removes the separator to 
    # ask if the string is only digits, otherwise isdigit() would return False as '.' and ',' are not digits
    kilometres = float(kilometres.replace(',', '.'))  # If float separator is aa comma ',', displays error in casting
    if kilometres >= 0:
        print(kilometres, 'km are', kilometres / kilometres_to_miles, 'mi')