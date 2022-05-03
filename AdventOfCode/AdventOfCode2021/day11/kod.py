lines = []
b = True
while b:
    try :
        temp = list(map(int,input()))
        lines.append(temp)
    except:
        b = False

rows = len(lines)
cols = len(lines[0])

def incSurrounding(row:int,col:int) -> list((int,int)):
    minRow = max(0, row-1)
    maxRow = min(rows-1, row+1)
    minCol = max(0,col-1)
    maxCol = min(cols-1, col+1)
    surround = [(r,c) for r,c in zip(range(minRow,maxRow),range(minCol,maxCol))]
    return surround.remove((row,col))




for row in range(rows):
    for col in range(cols):
        minRow = max(0, row-1)
        maxRow = min(rows, row+2)
        minCol = max(0,col-1)
        maxCol = min(cols, col+2)
        surround = [(r,c) for r,c in zip(range(minRow,maxRow),range(minCol,maxCol))]
        s = [(r,c) for c in range(minCol, maxCol) and  r in range(minRow, maxRow)]
        print(surround)

"""
Map över alla element i alla rader. x-> x+1
Hitta alla 10, låt dom blinka och ställas om till noll.
Varje gång ett element ställer om, addera ett till alla omgivande element.
iterera till inga 
"""

