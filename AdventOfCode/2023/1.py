in_arr = []
while(True):
    try:
        in_arr.append(input())
    except:
        break
res_arr = []

######PART ONE########
# for line in in_arr:
#     t = []
#     for c in line:
#         if c.isdigit():
#           t.append(int(c))
#     line_nmr = t[0]*10 + t[-1]
#     res_arr.append(line_nmr)
# print(sum(res_arr))  

#####Part Two###########

num_set = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}
#lengths of 3 4 or 5 

for line in in_arr:
    t = []
    i = 0
    for c in line:
        if c.isdigit():
          t.append(int(c))
        else:
            if line[i:i+3] in num_set:
                if line[i:i+3] == 'one':
                    t.append(1)
                elif line[i:i+3] == 'two':
                    t.append(2)
                elif line[i:i+3] == 'six':
                    t.append(6)
            elif  line[i:i+4] in num_set:
                if line[i:i+4] == 'four':
                    t.append(4)
                elif line[i:i+4] == 'five':
                    t.append(5)
                elif line[i:i+4] == 'nine':
                    t.append(9)
            elif line[i:i+5] in num_set:
                if line[i:i+5] == 'three':
                    t.append(3)
                elif line[i:i+5] == 'seven':
                    t.append(7)
                elif line[i:i+5] == 'eight':
                    t.append(8)
        i+=1
    line_nmr = t[0]*10 + t[-1]
    res_arr.append(line_nmr)
print(sum(res_arr))