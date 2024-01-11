
#seeds:
seeds = []
#default_maps:
# seed_to_soil    =   dict()
# soil_to_fert    =   dict()
# fert_to_water   =   dict()
# water_to_light  =   dict()
# light_to_temp   =   dict()
# temp_to_hum     =   dict()
# hum_to_loc      =   dict()

dicts_list = list(range(7))

def inp_to_dict(inp: list) -> dict() :
    ...
    #first element is which dict this represents.
    #all other lines are three values x y z
    #x is dest start value
    #y is source start value
    #z is range, i.e. how many more values are supposed to map beginning at dict[y] = x
    # want to build map as: y -> (x,z)
    
    dict_string = inp.pop(0)
    
    source_to_dest = {}
    for x, y, z in [map(int,x.split(' ')) for x in inp]:
        
        source_to_dest[y] = (x,z)

    return source_to_dest


with open('inp', 'r') as file:
    ls = file.read().strip()

    L = ls.split('\n')
    parts = ls.split('\n\n')
    seed, *others = parts
    seed = [int(x) for x in seed.split(':')[1].split()]
    
def find_loc(seed, part):
    for line in part:
        dest, source, diff = [int(x) for x in line.split()]
        if source<=seed<=source+diff:
            return dest+(seed-source)
    return seed

def find_loc_range(seed_range, part):
    locs = []
    for line in part:
        dest, source, size = [int(x) for x in line.split()]
        src_end = source+size
        part_res = []
        while seed_range:
            (start, end) = seed_range.pop()
            
            before = (start, min(end, source)) #the part of this range 'before' this 'part' 
            inter = (max(start, source), min(src_end, end)) #the intersection between range and this part
            after = (max(src_end, start), end) #the part of this range that is 'after' this 'part' 
            if before[1]>before[0]: #if range exists before part, add this
                part_res.append(before)
            if inter[1]>inter[0]: #if intersection between range and part exists, add this and transform
                locs.append((inter[0]-source+dest, inter[1]-source+dest))
            if after[1]>after[0]: #if range exists after part, add this
                part_res.append(after) 
        seed_range = part_res
    return locs + part_res

locations  = []

for s in seed:
    # s = int(s)
    for o in others:
        part = o.split('\n')
        s = find_loc(s, part[1:])
    locations.append(s)
print('part one: ', min(locations))
#107430936

seed_ranges = [(seed[x],seed[x]+seed[x+1]) for x in range(len(seed)) if x%2 == 0]
#tuples of start range and the final element in range plus 1

locations = []

t = seed_ranges
for o in others:
    part = o.split('\n')
    t = find_loc_range(t, part[1:])
locations=t
print('part2: ', min(locations)[0])