totCount = 0
bool = True

while bool:
    try:
        inp = input()
    except:
        bool = False
        print(totCount)
        break
    

    num_range, test_char, passW = inp.split(" ") #splits into strings

#Kolla position ett och två. exakt en av dessa ska vara 

    tmp = num_range.split("-")

    first = int(tmp[0])-1
    second = int(tmp[1])-1

#    first, second = num_range.split("-")

    char_to_check = test_char[0]

    char_check = 0
    for i in [first, second]:
        if passW[i] == char_to_check:
            char_check += 1
    
    if char_check == 1:
        totCount += 1

    print(f'siffror:{num_range, first, second}, Bokstav:{char_to_check}, passWord:{passW}, totCount:{totCount}')

