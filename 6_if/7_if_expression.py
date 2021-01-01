# It is intended for assigning an appropiate value to status, 
# an if expression returns a value and and stament no,
# the if expressions have the following structure: result1 if condition_is_met else result2
num = int(input('Enter a number: '))

status = 'It is even' if not (num % 2) else 'It is odd'
print(status)