#mod31.
#gå tre åt höger och en ner, hur många träd möter man?
#Concatenate strings using + 

bool = True
mapList = []
while bool:
    try:
        inp = input()
        mapList.append(inp)
    except:
        bool = False
        break

increments_ = [[1,1],[3,1],[5,1],[7,1],[1,2]]

prod = 1
for i in increments_:
    x = 0
    y = 0
    str = ''
#    for s in mapList:
    while y < len(mapList):
#        str = str + s[x%31]
        str = str + mapList[y][x%31]
        x += i[0]
        y += i[1]

    nmbr_trees = str.count('#')
    prod *= nmbr_trees

    print(f'{str},vägens längd:{len(str)}, antal träd:{nmbr_trees}')
print(prod)