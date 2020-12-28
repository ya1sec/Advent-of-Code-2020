fn = "input.txt"
dat = open(fn).read().strip().split("\n")
dat = [x for x in dat]


def p1(dat):
    seats = []
    for line in dat:
        row = [i for i in range(128)]
        col = [i for i in range(8)]
        for x in line:
            # print(x)
            if x == "F":
                row = row[:len(row)//2]
            if x == "B":
                row = row[len(row)//2:]
            if x == "L":
                col = col[:len(col)//2]
            if x == "R":
                col = col[len(col)//2:]
            # print(col, row)
        seat = (row[0] * 8) + col[0]
        seats.append(seat)
    seats.sort()
    print(seats)


def p2(dat):
    seats = []
    for line in dat:
        row = [i for i in range(128)]
        col = [i for i in range(8)]
        for x in line:
            # print(x)
            if x == "F":
                row = row[:len(row)//2]
            if x == "B":
                row = row[len(row)//2:]
            if x == "L":
                col = col[:len(col)//2]
            if x == "R":
                col = col[len(col)//2:]
            # print(col, row)
        seat = (row[0] * 8) + col[0]
        seats.append(seat)
    seats.sort()
    enum = list(enumerate(seats))
    for x in enum:
        if x[0] + 72 == x[1]:
            print(x, "confirmed")
        if x[0] + 72 != x[1]:
            print(x, "??????????????????????????????????????????")


p2(dat)

