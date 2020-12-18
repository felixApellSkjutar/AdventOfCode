#128 rader 0-127
#8 kolumner 0-7
#seat ID:  multiply the row by 8, then add the column


bool = True
inArr = []
while bool:
    try:
        inArr.append(input())
    except:
        bool = False

def rowCalc(inStr):
    currRange = range(0,128)
    for c in inStr:
        half = int(len(currRange)/2)
        if c == 'B':
            currRange = currRange[half:]
        elif c == 'F':
            currRange = currRange[:half]
    return currRange[0]

def colCalc(inStr):
    currRange = range(0,8)
    for c in inStr:
        half = int(len(currRange)/2)
        if c == 'R':
            currRange = currRange[half:]
        elif c == 'L':
            currRange = currRange[:half]
    return currRange[0]

currID = 0
idArr = []

for elem in inArr:
    currID = (rowCalc(elem[0:7]) * 8) + colCalc(elem[7:])
    idArr.append(currID)

idArr.sort()
itArr = filter(lambda x: x>0 and x<1032, idArr)

for i in itArr:
    next_index = idArr.index(i) +1
    if idArr[next_index] == i+2:
        print(i+1)
        break
