

myList = list()

bool = True

while bool:
    try:
        myList.append(int(input()))
    except:
        bool = False


for i in myList:
    cons = 2020
    newlist = myList
    newlist.remove(i)
    cons = cons - i
    for j in newlist:
        if cons - j == 0:
            print(f'{i} * {j} = {i*j}')
            break
