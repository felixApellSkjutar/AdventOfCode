inArr = []
b = True
while b:
    try :
        inArr.append(input())
    except:
        b = False

data = []
# 1 = 2
# 4 = 4
# 7 = 3
# 8 =  7
for segment in inArr:
    for s in segment.split(' | ')[1].split():
        data.append(s)

data = []
for segment in inArr:
    s = segment.split()
    s.remove('|')
    temp = list(s).sort()
    data.append(str(temp))

print(data)
res = []
nmbrs = list(range(10))
for segment in data:
    for d in segment:
        if len(d) == 2:
            nmbrs[1] = d
        elif len(d) == 3:
            nmbrs[7] = d
        elif len(d) == 4:
            nmbrs[4] = d
        elif len(d) == 7:
            nmbrs[8] = d
    for d in segment:
        if len(d) == 5 and nmbrs[1][0] in d and nmbrs[1][1] in d:
            nmbrs[3] = d
        elif len(d) == 6 and nmbrs[4][0] in d and nmbrs[4][1] in d and nmbrs[4][2] in d and nmbrs[4][3] in d:
            nmbrs[9] = d
        elif len(d) == 6 and nmbrs[1][0] in d and nmbrs[1][1] in d:
            nmbrs[0] = d
        elif len(d) == 5 and (nmbrs[1][0] in d or nmbrs[1][1] in d):
            s = list(filter(lambda x: x not in nmbrs[1], nmbrs[4]))
            if s[0] in d and s[1] in d:
                nmbrs[5] = d
            else:
                nmbrs[2] = d
        elif len(d) == 6: 
            nmbrs[6] = d
    n = ''
    for s in segment[10:14]:
        n += str(nmbrs.index(s))
    res.append(n)

print(nmbrs)
