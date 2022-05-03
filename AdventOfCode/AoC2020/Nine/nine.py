bool = True

inArr = []

while bool:
    try:
        inArr.append(int(input()))
    except:
        bool = False

#print(len(inStrArr)) 1000 element.

preamLow = 0
preamHigh = 25
preamArr = []

for elem in inArr[25:]:
    preamArr = inArr[preamLow:preamHigh]
    preamArr.sort()
    