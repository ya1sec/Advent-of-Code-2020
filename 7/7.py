fn = "input.txt"
dat = [x for x in open(fn).read().split("\n")]

#p1
def p1(dat):
    sgb = []
    second = []
    for x in dat:
        rule = x.split(" ")
        bagtype = rule[0:2]
        contains = rule[4:-1]
        if 'shiny' and 'gold' in contains:
            sgb.append(bagtype)
    for b in sgb:
        for r in dat:
            ru = r.split(" ")
            if b[0] and b[1] in ru[4:-1]:
                second.append(r)
    s = len(list(set(second)))
    return(s + len(sgb))

print(p1(dat))
