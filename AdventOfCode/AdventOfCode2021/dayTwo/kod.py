inArr = []
b = True
while b:
    try :
        inArr.append(input())
    except:
        b = False

forward = 0
depth = 0

for i in inArr:
    str, amnt = i.split()
    if str == "forward":
        forward += int(amnt)
    elif str == "up":
        depth -= int(amnt)
    elif str == "down":
        depth += int(amnt)

res = forward*depth
print(res)