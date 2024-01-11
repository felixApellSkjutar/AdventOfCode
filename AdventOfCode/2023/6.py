from functools import reduce
from operator import mul


with open('inp', 'r') as file:
    ls = file.read().strip()

    times = [int(x) for x in ls.split('\n')[0].split(':')[1].strip().split()]
    dists = [int(x) for x in ls.split('\n')[1].split(':')[1].strip().split()]
    
    races = zip(times, dists)
    
    single_race_time = int(''.join(map(str, times)))
    single_race_dist = int(''.join(map(str, dists)))

ways_to_win = []
for r in races:
    part_ways_to_win = 0
    for t in range(r[0]):
        #for all possible times, see if the distance travelled by holding the button for t milliseconds is enough to win
        if (r[0]-t)*t > r[1]:
            part_ways_to_win += 1
    ways_to_win.append(part_ways_to_win)
result = reduce(mul, ways_to_win)
print('part1', result)

def lower_bound(time, dist):
        for t in range(time):
        #for all possible times, see if the distance travelled by holding the button for t milliseconds is enough to win
            if (time-t)*t > dist:
                return t

def upper_bound(time, dist):
    t = time
    while t:
        print(t)
        if (time-t)*t > dist:
                return t
        t = t-1
lb = lower_bound(single_race_time, single_race_dist)
ub = upper_bound(single_race_time, single_race_dist)
print(lb, ub)
print('part2', ub-lb+1)