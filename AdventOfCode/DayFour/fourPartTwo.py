bool = True
str = ''
tot_valid = 0
while bool:
    try:
        inp = input()
        str += '|' +inp
    except:
        bool = False
        break


def byr_Check(birthYear) :

    return int(birthYear) in range(1920, 2003)


def iyr_Check(iyr):

    return int(iyr) in range(2010, 2021)

def eyr_check(eyr):

    return int(eyr) in range(2020,2031)

def hgt_check(hgt):
    try:
        i = int(hgt[:-2])
        str = hgt[-2:]
    except:
        return False

    if str == 'cm':
        return i in range(150, 195)
    elif str == 'in':
        return i in range(59,77)
    else:
        return False

def hcl_check (hcl):
    if hcl[0] == '#' and len(hcl[1:]) == 6:
        bool = True
        for ch in hcl[1:]:
            if not( ch.isalpha() or ch.isdigit() ):
                return False
        return bool
    else:
        return False

def ecl_check(ecl) :

    return ecl in {'amb','blu','brn','gry','grn','hzl','oth'}

def pid_check(pid):
    if len(pid) == 9:
        for str in pid:
            if not str.isdigit():
                return False
        return True
    else:
        return False
    
def check_checker(dict_ett):
    bool = False
    counter = 0

    for id in dict_ett:
        if id == 'byr':
            if byr_Check(dict_ett[id]):
                counter +=1
        elif id == 'iyr':
            if iyr_Check(dict_ett[id]):
                counter += 1
        elif id == 'eyr':
             if eyr_check(dict_ett[id]):
                 counter +=1
        elif id == 'hgt':
            if hgt_check(dict_ett[id]):
                counter +=1
        elif id == 'hcl':
            if hcl_check(dict_ett[id]):
                counter +=1
        elif id == 'ecl':
            if ecl_check(dict_ett[id]):
                counter += 1
        elif id == 'pid':
            if pid_check(dict_ett[id]):
                counter +=1
        else:
            pass
    if counter == 7:
        bool = True
    return bool


list_of_passports = str.split('||')



for i in list_of_passports:
    dick = dict()
    nmbr_valid = 0
    i = i.replace('|', ' ').split(' ')
    i = list(filter(lambda x: len(x)>=3, i))
    #
    for str in i:
        indentifier = str[0:3]
        if indentifier != 'cid':
            data = str[4:]
            dick.update({indentifier : data})
    
    if check_checker(dick):
        tot_valid += 1

print(tot_valid)