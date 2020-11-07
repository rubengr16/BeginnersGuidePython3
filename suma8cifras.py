suma = 0
lista = [] #empty array
for i in range(1,9): #i from 1 to 9 iterates
    print("\n Introduce el numero ", i, ":")
    lista.append(int(input())) #fill list & cast
for i in range(8):
    suma += lista[i]
print("\n Al sumar los elementos de esta lista", lista, "obtenemos", suma)
