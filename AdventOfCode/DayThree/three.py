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

x = 0
y = 0
str = ''
for s in mapList:
    str = str + s[x%31]
    x += 3

nmbr_trees = str.count('#')

print(f'{str},vägens längd:{len(str)}, antal träd:{nmbr_trees}')