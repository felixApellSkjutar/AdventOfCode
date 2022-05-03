inArr = []
b = True
while b:
    try :
        inArr.append(input())
    except:
        b = False

forward = 0
aim = 0
depth = 0

for i in inArr:
    str, amnt = i.split()
    if str == "forward":
        forward += int(amnt)
        depth += int(amnt) * aim
    elif str == "up":
        aim -= int(amnt)
    elif str == "down":
        aim += int(amnt)

res = forward*depth
print(res)