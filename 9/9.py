







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

def p1(i_list, i):
    index = 0
    result = False
    for num_1 in i_list:
        i_list.pop(index)
    for num_2 in i_list:
        if num_1 + num_2 == i:
            result = True
            i_list.insert(index, num_1)
            index += 1
    return result

def main(data, preamble):
    start_index = 0
    end_index = 25
    while end_index < (len(data)):
        i = data[end_index]
        i_list = data[start_index:end_index]
    if p1(i_list, i) is False:
        return i
    else:
        start_index += 1
        end_index += 1

def p2(data, target):
    for l_idx,v in enumerate(data):
        num_list = [v]
        total = v
        r_idx = l_idx + 1
    while total < target:
        total += data[r_idx]
        num_list.append(data[r_idx])
    if total == target:
        return sorted(num_list)[0] + sorted(num_list)[-1]
        r_idx += 1

if __name__ == '__main__':
    print('The solution to part 1 is : {}'.format(main(data, 25)))
    print('The solution to part 2 is : {}'.format(p2(data, main(data, 25))))
