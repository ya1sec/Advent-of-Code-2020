import itertools as it
fn = "input.txt"
dat = [x for x in open(fn).read().split("\n")]
dat.remove(dat[-1])
dat = [int(x) for x in dat]


def p1(c, i):
    index = 0
    res = False
    for n1 in c:
        c.pop(index)
        for n2 in c:
            if n1 + n2 == i:
                res = True
        c.insert(index, n1)
        index += 1
    return res

def main(dat, p):
    s = 0
    e = 5
    while e < (len(dat)):
        i = dat[e]
        c = dat[s:e]
        if p1(c, i) is False:
            return i
        else:
            s += 1
            e += 1

def p2(dat, t):
    for li, v in enumerate(dat):
        nums = [v]
        total = v
        ri = li + 1
        while total < t:
            total += dat[ri]
            nums.append(dat[ri])
            if total == t:
                return sorted(nums)[0] + sorted(nums)[-1]
            ri += 1

print(p2(dat, 31161678))



























































'''




























































def findPairs(p, x):
    return [pair for pair in it.combinations(p, 2) if sum(pair) == x]

for x in rest:
    i = dat.index(x)
    p = dat[i-25:i]
    print(findPairs(p, x))


first = dat[:5]
rest = dat[5:]
final = dat[-5:]


for x in rest:
    i = dat.index(x)
    p = dat[i-5:i]
    results = [sum(j) for j in list(it.combinations(p, 2))]
    res = [j for j in results if j == x]
    if len(res) == 0:
        print(x)






for x in dat:
    i = dat.index(x)
    print(i)
    current5 = dat[:r2]
    # p = current5[-5:]
    p = dat[r1:r2]
    print(p)
    if x == dat[r2]:
        if r2 < len(dat):
            r1 += 5
            r2 += 5
        if x in final:
            p = final
            r1 = 15
            r2 = len(dat) - 1

    print("x=" + str(x) + " r1=" + str(r1) + " datr1=" + str(dat[r1]) + " r2=" + str(r2) + " datr2=" +
            str(dat[r2]))










for x in dat:
    current5 = dat[:r2]
    p = current5[-5:]
    print(p)

    if x in dat[r1:r2]:
        preamble.append(x)
    if x == dat[r2]:
        if r2 < len(dat):
            r1 += 5
            r2 += 5
        if x in final:
            p = final
            r1 = 15
            r2 = len(dat) - 1

    print("x=" + str(x) + " r1=" + str(r1) + " datr1=" + str(dat[r1]) + " r2=" + str(r2) + " datr2=" +
            str(dat[r2]))

print(final)
for x in dat:
    s = x
    if len(preamble) > 5:
        del preamble[:]
    if x in dat[r1:r2]:
        preamble.append(x)
    if x == dat[r2]:
        if r2 < len(dat):
            r1 += 5
            r2 += 5
        if x in final:
            print(x)
            r1 = 15
            r2 = len(dat) - 1
    print("x=" + str(x) + " r1=" + str(r1) + " datr1=" + str(dat[r1]) + " r2=" + str(r2) + " datr2=" +
            str(dat[r2]))

print(preamble)
print(final)











for x in dat:
    s = x
    if len(preamble) > 5:
        del preamble[:]
    if x in dat[r1:r2]:
        preamble.append(x)
    if x == dat[r2]:
        if r2 < len(dat):
            r1 += 5
            r2 += 5
        if r2 == len(dat):
            print('mayday')
            r1 += 0
            r2 += 0
    print("x=" + str(x) + " r2=" + str(r2) + " datr2=" + str(dat[r2]))

for x in dat:
    if x in dat[r1:r2]:
        preambles.append(x)
    if x == dat[r2]:
        r1 += 5
        r2 += 5
        if r2 == len(dat):
            break
    print(x)
    print("x=" + str(x) + " r2=" + str(r2) + " datr2=" + str(dat[r2]))
'''
