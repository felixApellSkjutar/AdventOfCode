inArr = []
b = True
while b:
    try :
        inArr.append(input())
    except:
        b = False

data = list(map(int, inArr[0].split(',')))

i = 0

while i < 80:
    newFish = 0
    for ind in range(len(data)):
        if data[ind] > 0:
            data[ind] -= 1
        elif data[ind] == 0:
            data[ind] = 6
            newFish +=1
    for f in range(newFish):
        data.append(8)
    i+=1

print(len(data))

#-------------------Part 2-----------------------

fishMap = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}

data = list(map(int, inArr[0].split(',')))

for d in data:
    fishMap[d]= fishMap.get(d)+1


i = 0

while i < 256:
    newFish = fishMap[0]
    d = 0
    while d < 8:
        fishMap[d] = fishMap[d+1]
        d+= 1
    fishMap[6] += newFish
    fishMap[8] = newFish
    i+=1

print(sum(fishMap.values()))