import itertools as it
fn = "input.txt"
dat = [x for x in open(fn).read().split("\n")]
dat.remove(dat[-1])
dat = [int(x) for x in dat]
dat.sort()
dat.append(dat[-1] + 3)
dat.insert(0, 0)


o = 0
h = dat[-1]
v = []

def countx(v, x):
    c = 0
    for d in v:
        if (d == x):
            c += 1
    return c

for x in dat:
    i = dat.index(x)
    valid = [x + 1, x + 2, x + 3]
    print(x)
    l = []
    for a in valid:
        if a in dat:
            d = valid.index(a) + 1
            if d != 2:
                l.append(d)
                print(f'valid: {valid} a: {a}')
                print(f'valid: {a}, dif: {d}')
    if len(l) >= 1:
        v.append(l[0])
print(v)
print(countx(v, 3))
print(countx(v, 1))
