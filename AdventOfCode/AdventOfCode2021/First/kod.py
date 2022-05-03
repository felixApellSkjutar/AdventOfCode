inArr = []
b = True
while b:
    try :
        inArr.append(int(input()))
    except:
        b = False


countInc = 0

for i in range(1, len(inArr)) : 
    if inArr[i] > inArr[i-1] :
        countInc += 1


print(countInc)
