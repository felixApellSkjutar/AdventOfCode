inArr = []
b = True
while b:
    try :
        inArr.append(input())
    except:
        b = False

co2 = "" #least common bit
oxy = "" #most common bit

nmbrsLeft = inArr

count = 0
for ind in range(0,12):
    if len(nmbrsLeft) == 1:
        co2 += nmbrsLeft[0][ind:12]
        break
    charToAdd = ''
    temp = sum(list(map(lambda x : int(x[ind]), nmbrsLeft)))
    if temp < len(nmbrsLeft)/2:
        charToAdd = '1'
    else:
        charToAdd = '0'
    co2 += charToAdd
    nmbrsLeft = list(filter(lambda x : x[ind] != charToAdd, nmbrsLeft))
print(co2)

nmbrsLeft = inArr

count = 0
for ind in range(0,12):
    if len(nmbrsLeft) == 1:
        oxy += nmbrsLeft[0][ind:12]
        break
    charToAdd = ''
    temp = sum(list(map(lambda x : int(x[ind]), nmbrsLeft)))
    if temp < len(nmbrsLeft)/2:
        charToAdd = '0'
    else:
        charToAdd = '1'
    oxy += charToAdd
    nmbrsLeft = list(filter(lambda x : x[ind] != charToAdd, nmbrsLeft))
print(oxy)

dec_oxy = int(oxy,2)
dec_co2 = int(co2,2)
print(dec_oxy*dec_co2)