from collections import defaultdict
from functools import lru_cache

fn = "input.txt"
dat = open(fn).read().strip().split("\n")
dat = [x for x in dat]

dat = [int(i) for i in dat] 
print(dat)

# print(type(dat))
# print(dat)

for x in dat:
    x = int(x)
    y = 2020 - x
    num = str(y)
    if num in dat:
        print(num)
        print(x * y)

def findTrip(dat, l, s):
    for i in range(0, l-2):
        for j in range(i + 1, l-2):
            for k in range(j + 1, l):
                if dat[i] + dat[j] + dat[k] == s:
                    product = dat[i] * dat[j] * dat[k]
                    print(product)
                    print("trip: ", dat[i], ", ", dat[j], ", ", dat[k])
                    return True
    return False

s = 2020
l = len(dat)
findTrip(dat, l, s)
