import re

inp = []

with open('inp.in', 'r') as file:
    ls = file.read()
    
    # print(ls.split('\n'))
    for line in ls.split('\n'):
        nums = line.split(':')[1]
        winning_nums = re.search(r"(\s+\d+)+", nums).group(0)
        elf_nums = re.search(r"(\s+\d+)+", nums.split('|')[1]).group(0)
        inp.append((set(filter(lambda x: x != '' , winning_nums.split(' '))), filter(lambda x: x != '',elf_nums.split(' '))))




def part_1(inp: list):
    sum_winning_nums = 0
    for pair in inp:
        winning_nums = 0
        for num in pair[1]:
            if num in pair[0]:
                winning_nums += 1
        if winning_nums > 0:
            sum_winning_nums += pow(2, winning_nums - 1)
    print(sum_winning_nums)

#part_1(inp)
####part 2
#mappa scratchcard till hur många copies det finns.
#Om ett kort ger vinst, ge detta korts copies i copies till antalet vinst kort fram.
#det finns minst ett kort av varje, så alla börjar på 1

def part_2(inp: list):
    copies = {card : 1 for card in range(len(inp))}
    
    for i in range(len(inp)):
        winning_nums = 0
        for num in inp[i][1]:
            if num in inp[i][0]:
                winning_nums += 1
        if winning_nums > 0:
            for j in range(i+1, i+winning_nums+1):
                copies[j] += copies[i]
    print(sum(copies.values()))
            

part_2(inp)   