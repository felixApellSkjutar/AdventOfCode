inArr = []
b = True
while b:
    try :
        inArr.append(input())
    except:
        b = False

newList = list(filter(None, inArr)) #filtered from empty elements.

#fold along x=655

resArr = []
for elem in newList:
    x,y = elem.split(",")
    resArr.append([int(x),int(y)])


reSet = set()
for elem in resArr:
    if elem[0] > 655 :
        dif = elem[0]-655
        newPos=655-dif
        temp = [newPos,elem[1]]
        reSet.add(str(temp))
    elif elem[0] < 655:
        reSet.add(str(elem))

print(len(reSet))