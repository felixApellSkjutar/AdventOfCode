inArr = []
b = True
while b:
    try :
        inArr.append(input())
    except:
        b = False

gamma = ""
epsilon = ""


for i in range(0,12):
    count = 0
    for s in inArr:
        if int(s[i]) == 1:
            count += 1
    if count > 500:
        gamma += str(1)
    else:
        gamma += str(0)

for s in gamma:
    if int(s) == 1:
        epsilon += str(0)
    else:
        epsilon += str(1)

dec_gamma = int(gamma,2)
dec_epsilon = int(epsilon,2)

print(dec_gamma * dec_epsilon)