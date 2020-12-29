fn = "input.txt"
dat = open(fn).read().split(".\n")
dat.remove(dat[-1])

def p1(dat):
    bags = {}
    for bag in dat:
        bag = bag.replace(" bags", "").replace(" bag", "").replace(".", "")
        bag = bag.split(" contain ")
        k = bag[0]
        v = bag[1]
        bags[k] = v
        # print(bag)

    def parent(child):
        for p in bags:
            content = bags[p]
            if child in content:
                parent(p)
                bagset.add(p)
        return

    bagset = set()
    parent("shiny gold")
    return(str(len(bagset)))

# print(p1(dat))

bags = {}
for bag in dat:
    bag = bag.replace(" bags", "").replace(" bag", "").replace(".", "")
    bag = bag.split(" contain ")
    k = bag[0]
    v = bag[1]
    bags[k] = v

def parent(child):
    for p in bags:
        content = bags[p]
        if child in content:
            parent(p)
            bagset.add(p)
    return

def addchild(p):
    content = bags[p].split(", ")
    if content[0] == "no other":
        return
    else:
        for child in content:
            bagname = child[2:]
            number = int(child[0])
            if bagname in childcount:
                childcount[bagname] += number
            else:
                childcount[bagname] = number
            for i in range(number):
                addchild(bagname)
        return

bagset = set()
childcount = {}
addchild("shiny gold")
print(str(sum(childcount.values())))

