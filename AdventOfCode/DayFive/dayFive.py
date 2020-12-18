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

maxID = 0
currID = 0
for elem in inArr:
    
    currID = (rowCalc(elem[0:7]) * 8) + colCalc(elem[7:])
    print(f'{elem}: {rowCalc(elem[0:7])} col: {colCalc(elem[7:])} ID: {currID}')
    if currID > maxID:
        maxID = currID

print(maxID)