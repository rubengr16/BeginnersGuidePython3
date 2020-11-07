symbol = input("type down a character: ")
height = int(input("chose triangle's height: "))

for i in range(0, height):
     print(' ', end = '') 
print(symbol)
     
for i in range(1, height):
    for j in range(height - i):
        print(' ', end = '') 
    print(symbol, end = '')    
    for j in range((i - 1) * 2 + 1):    
        print(' ', end = '') 
    print(symbol, end = '')    
    print("\n") 
for i in range(0, height * 2 + 1):
    print(symbol, end = '') 