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

print( list(filter(lambda x : x[1] != '0', nmbrsLeft) ) )

for ind in range(0,12):
    zeros = list(filter(lambda x : x[ind] != '1', nmbrsLeft))

    ones = list(filter(lambda x : x[ind] != '0', nmbrsLeft))
    charToAdd = ''
    if len(ones) < len(zeros):
        charToAdd += '0'
        nmbrsLeft = zeros
    else:
        charToAdd += '1'
        nmbrsLeft = ones
    oxy += charToAdd

nmbrsLeft = inArr

for ind in range(0,12):
    
    zeros = list(filter(lambda x : x[ind] != '1', nmbrsLeft))

    ones = list(filter(lambda x : x[ind] != '0', nmbrsLeft))
    charToAdd = ''
    if len(ones) < len(zeros):
        charToAdd += '1'
        nmbrsLeft = ones
    else:
        charToAdd += '0'
        nmbrsLeft = zeros
    co2 += charToAdd
print(oxy, co2)

dec_oxy = int(oxy, 2)
dec_co2 = int(co2, 2)

print(dec_oxy * dec_co2)