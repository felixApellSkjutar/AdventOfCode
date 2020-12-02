

myList = list()

bool = True

while bool:
    try:
        myList.append(int(input()))
    except:
        bool = False



for i in myList:
    cons = 2020
    newList = myList
    newList.remove(i)
#    cons = cons - i
#    newList = [n for n in newList if n <= cons]
    for j in newList:
#        newList.remove(j)
#        cons = cons - j
#        newList = [n for n in newList if n <= cons]
        for k in newList:
            if cons - k -i-j == 0 :
                print(f'{i}*{j}*{k}={i*j*k}')
                break

#slimList = [n for n in myList if n < 673]

