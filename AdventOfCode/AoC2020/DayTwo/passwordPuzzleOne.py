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



    min, max = num_range.split("-")

    char_to_count = test_char[0]

    times_occured = passW.count(char_to_count)

    if times_occured >= int(min) and times_occured <= int(max):
        totCount = totCount + 1


    print(f'siffror:{num_range, min, max},räknat:{times_occured}, Bokstav:{test_char}, passWord:{passW}, totCount:{totCount}')

