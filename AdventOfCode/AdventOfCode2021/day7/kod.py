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

maxPos = None
maxVal = 0
for p in posMap.keys():
    if posMap[p] > maxVal:
        maxVal = posMap[p]
        maxPos = p
print(maxPos, posMap[maxPos], maxVal)
fuel = 0

fuelList = []
for pos in posMap.keys():
    fuel = 0
    for p in posMap.keys():
        fuel += posMap[p] * abs(p-pos)
    fuelList.append(fuel)

print(min(fuelList))
        
            