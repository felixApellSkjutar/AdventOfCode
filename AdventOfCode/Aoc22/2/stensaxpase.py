
f = open('in.in','r')


#A rock  - X
#B Paper  -Y
#C Scissors -Z
p = dict()
p['X'] = 1
p['Y'] = 2
p['Z'] = 3
p['A'] = 1
p['B'] = 2
p['C'] = 3

#OUtcome
# 0 -> 3(draw) -> 6 (win)

def win(a: int, b: int) -> int:
    if a == b:
        return 3 + b
    elif a == 1:
        if b == 2:
            return 6 + b
        elif b == 3:
            return  b
        else:
            print('vafan')
            return 0
    elif a == 2:
        if b == 1:
            return  b
        elif b == 3:
            return 6 + b
        else:
            print('vafan2')
            return 0
    elif a == 3:
        if b == 2:
            return  b
        elif b == 1:
            return 6 +b
        else:
            print('vafan3')
            return 0
    else:
        print('vafan 4')
        return 0
res = 0

decide = dict()
#########2
#X = Förlora
#Y = drawing
#Z = win
inlist = f.read().split('\n')
print(inlist)
for i in inlist:
    it = i.split(" ")
    a, b = p[it[0]], p[it[1]]
    temp = 0
    if b == 2:
        temp =  win(a, a)
    elif b == 1:
        if a > 1:
            temp = win(a, a-1)
        else:
            temp = win(a,3)
    else:#B ==3
        if a < 3:
            temp = win(a, a+1)
        else:
            temp = win(3,1)
    res += temp




print(res)