bool = True

inArr = []
inStr = ''
while bool:
    try:
        ins = input()
        if ins != '' and inStr == '':
            inStr += ins
        elif ins != '':
            inStr += ' ' + ins
        elif ins == '':
            inArr.append(inStr)
            inStr = ''
    except:
        inArr.append(inStr)
        bool = False

print(inArr)

resArr = []

#for arr in inArr:
#    groupSum = 0
#    groupSet = set(list(filter(lambda x: x != ' ', arr)))
#    groupStr = arr.split(" ")
#    nmrInGroup = len(groupStr)
#    
#    for s in groupSet:
#        truthCounter = 0
#        for n in groupStr:
#            if s in n:
#                truthCounter +=1
#        if truthCounter == len(n):
#            groupSum += 1
#        
res = 0
for arr in inArr:
    nmbrMembers = len(arr.split(' ')) #ger antalet medlemmar i gruppen
    groupMap = {}

    for x in filter(lambda n : n != ' ', arr) :
        groupMap.update({x : arr.count(x)}) #mappar char till hur många gånger den dyker upp inom gruppen.
    print(groupMap)
    for key in groupMap:
        if groupMap[key] == len(arr.split(' ')):
            res += 1
print(res)
