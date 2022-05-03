inArr = []
b = True
while b:
    try :
        inArr.append(input())
    except:
        b = False

data = list(map(int,inArr[0].split(',')))

posMap = {0:0}

for d in data:
    if d in posMap:
        posMap[d] += 1
    else:
        posMap[d] = 1
#print(posMap)

fuelList = []
for pos in range(0,max(posMap.keys())):
    fuel = 0
    for p in posMap.keys():
        fuel += posMap[p] * sum(list(range(1,abs(p-pos)+1)))
    fuelList.append(fuel)

print(min(fuelList))
        
            