inArr = []
b = True
while b: 
    try:
        inArr.append(int(input()))
    except:
        b = False

countArr = []
for i in range(0,len(inArr)-2):
    countArr.append(inArr[i]+inArr[i+1]+inArr[i+2])

count = 0
for i in range(1,len(countArr)):
    if countArr[i] > countArr[i-1]:
        count +=1

print(count)