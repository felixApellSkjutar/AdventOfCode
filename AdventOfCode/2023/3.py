ls = []
while(True):
    try:
        ls.append(input())
    except:
        break

#characters not defined as special symbols.
non_symbols = set(".0123456789")

#every location of a "special symbol", mapped to that symbol and a list of the numbers adjacent. 
symbol_locations = {
    (i,j):(x,[])
    for i,l in enumerate(ls)
    for j,x in enumerate(l)
    if x not in non_symbols
}

sym_loc_set = symbol_locations.keys()

n = 0
part_sum = 0
for i, l in enumerate(ls):
    for j, c in enumerate(l):
        if c.isdigit():
            n = n*10+int(c)
        elif n > 0:
            i_bound = range(i-1,i+2)
            j_bound = range(j-len(str(n))-1, j+1)
            found = False
            for k in i_bound:
                for l in j_bound:
                    if (k,l) in sym_loc_set:
                        symbol_locations[(k,l)][1].append(n)
                        found = True
            if found:
                part_sum += n
            n = 0
    if n > 0:
        i_bound = range(i-1,i+2)
        j_bound = range(j-len(str(n)), j+1)
        found = False
        for k in i_bound:
            for l in j_bound:
                if (k,l) in sym_loc_set:
                    symbol_locations[(k,l)][1].append(n)
                    found = True
                    print(k,l,n)
        if found:
            part_sum += n
        n = 0
# print(symbol_locations)
# print("part: ",part_sum)

gear_sum = 0
for gear in sym_loc_set:
    if symbol_locations[gear][0] == '*'and len(symbol_locations[gear][1]) == 2:
        gear_sum += symbol_locations[gear][1][0]*symbol_locations[gear][1][1]

print(gear_sum)