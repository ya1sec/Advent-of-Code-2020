fn = "input.txt"
dat = open(fn).read().split(".\n")
dat.remove(dat[-1])

bags = {}
for bag in dat:
    bag = bag.replace(" bags", "").replace(" bag", "").replace(".", "")
    bag = bag.split(" contain ")
    k = bag[0]
    v = bag[1]
    bags[k] = v
print(bags)


def parent(child):
    for p in bags:
        content = bags[p]
        if child in content:
            parent(p)
            bagset.add(p)
    return

bagset = set()
parent("shiny gold")
print(str(len(bagset)))
