fn = "input.txt"
dat = open(fn).read().split("\n\n")

def p1(dat):
    g = []
    for x in dat:
        n = len(set(x.replace("\n", "")))
        g.append(n)
    return(sum(g))


def p2(dat):
    total = 0
    for x in dat:
        y = x.split()
        common = set.intersection(*map(set, y))
        total += len(common)
    return(total)

print(p1(dat))
print("p2: ", p2(dat))
