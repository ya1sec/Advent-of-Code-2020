from collections import defaultdict
from functools import lru_cache

fn = "input.txt"
dat = open(fn).read().strip().split("\n")
dat = [x for x in dat]

# dat = [int(i) for i in dat] 
# print(dat)


def part1(dat):
    bigc = 0
    for line in dat:
        line = line.split(' ')
        low = line[0].split('-')[0]
        low = int(low)
        upp = line[0].split('-')[1]
        upp = int(upp)
        target = line[1][0]
        password = line[2]
        print(password)
        print(password[0])
        c = 0
        for x in password:
            if x == target:
                c+=1
        if c >= low and c <= upp:
            bigc+=1
            print(True)
        print(c, line) 
    print(bigc)

def part2(dat):
    bigc = 0
    for line in dat:
        line = line.split(' ')
        low = int(line[0].split('-')[0])
        upp = int(line[0].split('-')[1])
        li = low - 1
        ui = upp - 1
        password = line[2]
        target = line[1][0]
        if (password[li] == target and password[ui] != target) or (password[li] != target and
                password[ui] == target):
            bigc+=1
            print(True)
        print(password, line)
    print(bigc)


part1(dat)
part2(dat)
