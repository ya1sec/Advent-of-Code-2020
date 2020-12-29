fn = "input.txt"
dat = [x for x in open(fn).read().split("\n")]
dat.remove(dat[-1])

# acc +/- accumulator by number
position = 0
accumulator = 0
positions = []

def nop():
    global position 
    position += 1
    boot(position)

def acc(value):
    global accumulator
    accumulator += value
    nop()

def jmp(value):
    global position
    position += value
    boot(position)

def boot(Position):
    global dat, positions
    command = dat[Position]
    action = command[0:3]
    value = int(command[3:])
    if Position in positions:
        return
    else:
        positions.append(Position)
    if action == "nop":
        nop()
    elif action == "acc":
        acc(value)
    else:
        jmp(value)


boot(0)
