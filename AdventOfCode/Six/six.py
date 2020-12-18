bool = True
inArr = []
while bool:
    try:
        inArr.append(input())
    except:
        bool = False

inArr.append('')
groupArr = []
inStr = ''
for line in inArr:
    if line != '':
        inStr = inStr + line
    elif line == '':
        groupArr.append(inStr)
        inStr = ''
#print(len(groupArr)) # 464 rader

groupSum = 0
for s in groupArr:
    groupSum += len(set(list(s)))

groupSet = [len(set(list(x))) for x in groupArr]

print(groupSet)
#groupArr = list(filter(lambda x: x != '',inArr))
#

#
print(groupSum)