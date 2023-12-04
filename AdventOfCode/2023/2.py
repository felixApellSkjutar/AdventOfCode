in_arr = []
while(True):
    try:
        in_arr.append(input())
    except:
        break



####Part One####
# cubes = {'red':12, 'green':13, 'blue':14} #If these are the cubes, which games of input are possible?

# games = list(map(lambda x: x.split(':')[1], in_arr))

# possible_games = set()
# index = 1

# for g in games:
#     sub_games = g.split(';') #list of the subgames for each game
#     b = True
#     for s in sub_games:
#         for i in s.split(','):
#             temp = i.split()
#             if int(temp[0]) > cubes[temp[1]]:
#                 #print(temp[0], temp[1])
#                 b = False
#     if b:
#         possible_games.add(index)
#     index += 1
# print(sum(possible_games))

####Part Two####
cubes = {'red':12, 'green':13, 'blue':14} #If these are the cubes, which games of input are possible?

games = list(map(lambda x: x.split(':')[1], in_arr))


game_powers = []

for g in games:
    sub_games = g.split(';') #list of the subgames for each game

    max_cubes = cubes = {'red':0, 'green':0, 'blue':0} #If these are the cubes, which games of input are possible?

    for s in sub_games:
        for i in s.split(','):
            temp = i.split()
            if int(temp[0]) > max_cubes[temp[1]]:
                max_cubes[temp[1]] = int(temp[0])
    game_powers.append(max_cubes['red'] * max_cubes['green'] * max_cubes['blue'])
    
print(sum(game_powers))