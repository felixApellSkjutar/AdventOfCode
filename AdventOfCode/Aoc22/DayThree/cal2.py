
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
inp = []
for l in lines:
    inp.append(l.replace('\n',''))

#split inp into chunks of 3
chunks = [inp[x:x+3] for x in range(0, len(inp), 3)]

#create intersection of each chunk
for c in chunks:
    interSects += list(set.intersection(*map(set, c)))
res = 0
for i in interSects:
    i = ord(i)
    if i >= 97:
        res += i%96
    else:
        res += i%64 + 26
print(res)


#temp = conversion(ll)
#mid = int(len(temp)/2)
#l1, l2 = set(temp[0:mid]), set(temp[mid:])
#res = l1.intersection(l2)
#interSects += list(res)
#

#
#
#