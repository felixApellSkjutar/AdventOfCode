import re
f = open('realIn.in', 'r')

ll = f.readlines()
inp = []
com = []
pre = True
for l in ll:
    l = l.replace('\n', '')
    l = l.replace('    ', '1')
    #print(ll)
    if l == '':
        pre = False
        continue
    if pre:
        inp.append(l)
    else:
        t = l.split(" ")
        #take oddd indices from t
        com.append(t[1::2])

temp = inp.pop(-1)
nmbrStacks = int(temp.strip()[-1])
#print(com)

temp  = []
for i in inp:
    #remove everything that's not letters
    temp.append(re.sub('[^a-zA-Z1-9]', '', i))

#print(temp)
stacks = []
for i in range(0,nmbrStacks):
    stacks.append(list())

while(len(temp) != 0) :
    t = temp.pop()
    for i in range(0, nmbrStacks):
        if t[i] != '1':
            stacks[i].append(t[i])
print(stacks)

for i in range(0, len(com)):
    p = com.pop(0)
    amount =    int(p[0])
    fromstack = int(p[1])-1
    to =        int(p[2])-1
    l = len(stacks[fromstack])

    t  = stacks[fromstack][l-amount:]
    for i in range(0,amount):
        stacks[fromstack].pop()
    stacks[to] += t

print(stacks)


res = ''
for i in stacks:
    res += i.pop()
print(res)
