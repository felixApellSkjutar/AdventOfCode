bool = True

inArr = []
inStr = ''
while bool:
    try:
        ins = input()
        if ins != '' and inStr == '':
            inStr += ins
        elif ins != '':
            inStr += ' ' + ins
        elif ins == '':
            inArr.append(inStr)
            inStr = ''
    except:
        inArr.append(inStr)
        bool = False

print(inArr)


