
f = open('in.in', 'r')

lines = f.readlines()

def conversion(l : list):
    t = []
    for x in l:
        s = ord(x)
        t.append(s)
    return t
def reconversion(c: set)->chr:
    t = []
    for s in c:
        t.append(chr(s))
    return t

print(lines)
interSects = []
for l in lines:
    ll = l.replace('\n','')
    temp = conversion(ll)
    mid = int(len(temp)/2)
    l1, l2 = set(temp[0:mid]), set(temp[mid:])
    res = l1.intersection(l2)

    interSects += list(res)

res = 0
for i in interSects:
    if i >= 97:
        res += i%96
    else:
        res += i%64 + 26
print(res)


