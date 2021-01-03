import itertools as it
fn = "input.txt"
dat = [x for x in open(fn).read().split("\n")]
dat.remove(dat[-1])
dat = [int(x) for x in dat]

preamble = 25

# Part 1
def checkNum(pos):
    global dat 
    startpos = pos - preamble
    combs = [lst for lst in it.combinations(dat[startpos:pos], 2)]
    # create list of unique combinations of numbers
    sums = [sum(i) for i in combs]
    if dat[pos] in sums:
        checkNum(pos + 1)
    else:
        print('part 1: ' + str(dat[pos]))
    return [dat[pos], pos]

checkNum(preamble)




