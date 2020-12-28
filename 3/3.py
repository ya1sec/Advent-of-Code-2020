from collections import defaultdict
from functools import lru_cache

fn = "input.txt"
dat = open(fn).read().strip().split("\n")
dat = [x for x in dat]

# dat = [int(i) for i in dat] 

def p1(right=3, down=1):
    pos = 0
    tree = 0
    for i in range(0, len(dat), down):
        line = dat[i]
        if '#' == line[pos]:
            tree += 1
        pos += right
        pos = pos % len(line)
    print(tree)
    return tree

p1()

product = p1(right=3, down=1) * p1(right=1, down=1)* p1(right=5, down=1) * p1(right=7, down=1) * p1(right=1, down=2)  

print(product)
