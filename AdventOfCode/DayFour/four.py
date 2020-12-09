bool = True
str = ''
while bool:
    try:
        inp = input()
        str += '|' +inp
    except:
        bool = False
        break


#split('||')
tot_valid = 0

demand_set = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
#
#    byr (Birth Year)
#    iyr (Issue Year)
#    eyr (Expiration Year)
#    hgt (Height)
#    hcl (Hair Color)
#    ecl (Eye Color)
#    pid (Passport ID)
#    cid (Country ID)
#


list_of_passports = str.split('||')

for i in list_of_passports:
    nmbr_valid = 0
    i = i.replace('|', ' ').split(' ')
    i = list(filter(lambda x: len(x)>=3, i))
    i = list(map(lambda x: x[0:3], i))
    #print(i)
    for str in i:
        if str in demand_set:
            nmbr_valid += 1
    if nmbr_valid == 7:
        tot_valid +=1


print(tot_valid)