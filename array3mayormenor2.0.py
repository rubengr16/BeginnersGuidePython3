#no aux
list = []
while len(list) != 3 or list[0] == list[1] or list[1] == list[2]: #fill no repetitions
    for i in range(3):
        list.append(int(input("introduce valor:")))
while list[1] > list [0] or list[2] > list[1]:
    if list[2] > list[1]:
        list[1] += list[2]
        list[2] = list[1] - list[2]
        list[1] -= list[2]
    if list[1] > list[0]:
        list[0] += list[1]
        list[1] = list[0] - list[1]
        list[0] -= list[1]

print(list[0], "es el mayor de los números y ", list[2], "el menor")
    
