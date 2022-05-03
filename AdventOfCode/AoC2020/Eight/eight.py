#samla in data från fil
bool = True
inStrArr = []

while bool:
    try:
        inStrArr.append(input())
    except:
        bool = False

print(inStrArr)


def jmp(ind):
    #Hoppa till instruktionen nmbr steg från denna.
    ind = ind.strip()
    signed = ind[0]
    nmbr = ind[1:]

    if signed == '-':
        return -1 * int(nmbr)
    elif signed == '+':
        return int(nmbr)

def acc(accStr):
    #addera medföljande tal till acc, gå till nästa instruktion
    accStr = accStr.strip()
    global accNum

    signed = accStr[0]
    nmbr = accStr[1:]

    if signed == '-':
        accNum -= int(nmbr)
    elif signed == '+':
        accNum += int(nmbr)
    return 1

def nop():
    #Gör inte ett skit
    return 1

def decoder(instruction):
    inst = instruction[:3].strip()

    if inst == "acc":
        return acc(instruction[4:])
    elif inst == "jmp":
        return jmp(instruction[4:])
    elif inst == "nop":
        return nop()



visited = set()
currInd = 0
#GLOBAL

accNum = 0


bool = True
while bool:
    if currInd in visited:
        bool = False
        print(accNum)
    else:
        visited.add(currInd)
        instr = inStrArr[currInd]
        currInd += int(decoder(instr))
        

