fn = "input.txt"
dat = [x for x in open(fn).read().split("\n")]
dat.remove(dat[-1])

code = []
visited = {}

# PART 1

for x in dat:
    operation, value = x.split()
    code.append((operation, int(value)))


def run(code, visited, a=0, i=0):
    while i not in visited and i < len(code):
        visited[i] = a
        operation, value = code[i]
        if operation == "acc":
            a += value
        elif operation == "jmp":
            i += value - 1
        i += 1
    return a, i


a, _ = run(code, visited)
print(a)

# PART 2

s = set(visited.keys())

for j in s:
    operation, value = code[j]
    # skip ops that would continue in loops
    if (operation == "nop" and (i := j + value) not in visited) or \
            (operation == "jmp" and (i := j + 1) not in visited):
                a, i = run(code, visited, visited[j], i)
    if i >= len(code):
        print(a)
        break
