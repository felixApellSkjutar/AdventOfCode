

f = open('in.in', 'r')


#remove the newline character
lines = [x.replace('\n','') for x in f.readlines()]

sec = [x.split(',') for x in lines]

res = 0
#print(sec)
for i in sec:
    #trim all spaces
    print(i)
    i = [x.strip() for x in i]
    
    
    r1 = range(int(i[0].split('-')[0]), int(i[0].split('-')[1])+1)
    r2 = range(int(i[1].split('-')[0]), int(i[1].split('-')[1])+1)
    print(r2)
    ####Assignment1
    #check if r2 is in r1
    #if (r2[0] in r1 and r2[-1] in r1) or (r1[0] in r2 and r1[-1] in r2):
    #    res += 1
    ###ASSignment2
    if (r2[0] in r1 or r2[-1] in r1) or (r1[0] in r2 or r1[-1] in r2):
        res += 1
print(res)


