# Boolean values are True and False, in python they are called bool
boolean = True
print(boolean)
print('boolean type:', type(boolean))

# Boolean is a subtype of integer containing only 2 values: 1 = True and 0 = False
boolean = bool(0)
print(boolean)
print('boolean type:', type(boolean))

boolean = int(1)
print(boolean)
print('boolean type:', type(boolean))


# Casting string:  nonempty string converts to True and empty string converts to False
boolean = 'False'
print(boolean)
print('boolean type:', type(boolean))

boolean = bool(boolean)
print(boolean)
print('boolean type:', type(boolean)) 

boolean = bool('')
print(boolean)
print('boolean type:', type(boolean))