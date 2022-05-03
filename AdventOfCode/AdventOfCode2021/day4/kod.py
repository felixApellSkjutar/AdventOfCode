inArr = []
b = True
while b:
    try :
        inArr.append(input())
    except:
        b = False
    

nmbrs = inArr[0]

inArr.pop(0)
inArr.remove('')
print(nmbrs)

boards = []
n = 0
for ind in range(0,len(inArr)):
    boardInd = n*5+ind
    n+=1
    temp = []
    for elem in inArr[boardInd:boardInd+5]:
        unFixed = elem.split(" ")
        while '' in unFixed:
            unFixed.remove('')
        temp.append(unFixed)
    boards.append(temp)



print(boards[0])

res = []

for nmbr in nmbrs:
    for board in boards:
        for b in board:
            try:
                col = b.index(str(nmbr))
                row = board.index(b)
                #print(row,col)
            except:
                None

