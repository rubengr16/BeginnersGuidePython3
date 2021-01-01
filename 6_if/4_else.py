# The else part is optional and will be run if the conditional part of the if statement returns False,
# if an else is present, it is guaranteed that at least the if or the else will be executed 
num = int(input('Enter a number: '))

if num <= 0:
    if num == 0:
        print('It is zero')
    else:
        print('It is negative')
else:
    print('It is possitive') 