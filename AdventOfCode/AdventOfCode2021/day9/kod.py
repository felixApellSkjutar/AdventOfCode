inArr = []
b = True
while b:
    try :
        inArr.append(input())
    except:
        b = False
#print(inArr)
h ,w, part1 = len(inArr), len(inArr[0]), 0

for r in range(h):
    for c in range(w):
        if any (
            inArr[r][c] >= inArr[x][y]
            for i, j in ((-1,0), (1,0), (0,-1),(0,1))
            if 0 <= (x := r+i) < h and 0 <= (y := c+j) < w
        ):
            continue

        part1 += int(inArr[r][c]) +1

print(part1)