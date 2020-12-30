# Take input from the user in a given distance in kilometres
# convert the value returned from a string to float
# convert the value into miles (dividen the kilometers by 0.6214)
# print out a message saying to the user what the kilometres are in miles  
kilometres = float(input('Enter a distance in kilometres: '))
kilometres_to_miles = 0.6214

print(kilometres, 'km are', kilometres / kilometres_to_miles, 'mi')