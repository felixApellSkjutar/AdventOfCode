

max = 0

#f = open("in.in", 'r')

#l = f.read().split('\n')
l = []

resList = []
temp = []

t = True


f = open('in.in', 'r')
i = f.read().split('\n')

iList = []

temp = []
resList = []
for x in i:
    try:
        temp.append(int(x))
    except:
        resList.append(sum(temp))
        temp = []

max = 0
for x in resList:
    if x > max:
        max = x
resList.sort(reverse=True)

print(sum(resList[0:3]))

