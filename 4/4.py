from re import match

fn = "input.txt"
# dat = [x for x in dat]
with open(fn, 'r') as file:
    dat = [x.split() for x in file.read().split("\n\n")]

for x in dat:
    print(x)

passports= []

for x in dat:
    pp = {}
    for key_val in x:
        key_val = key_val.split(":")
        key = key_val[0]
        val = key_val[1]
    pp[key] = val
    passports.append(pp)

required = {"byr": lambda y: match("\d{4}", y) and 1920 <= int(y) <= 2002,
"iyr": lambda y: match("\d{4}", y) and 2010 <= int(y) <= 2020,
"eyr": lambda y: match("\d{4}", y) and 2020 <= int(y) <= 2030,
"hgt": lambda h: match("\d+(cm|in)", h) and \
                   ((h[-2:] == "cm" and 150 <= int(h[:-2]) <= 193) or \
                    (h[-2:] == "in" and 59 <= int(h[:-2]) <= 76)),
"hcl": lambda c: match("#[0-9a-f]{6}", c),
"ecl": lambda c: match("amb|blu|brn|gry|grn|hzl|oth", c),
"pid": lambda i: match("^\d{9}$", i)}


c = 0
c2 = 0
for x in passports:
    v1 = True
    v2 = True
    for field in required:
        validity_check = required[field]
        if field not in x:
            v1 = False
        elif not validity_check(x[field]):
            v2 = False
    if v1:
        c1 += 1
    if v2:
        c2 += 1

print(c)





























'''
fields = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        'cid'
        }

required = fields.difference({'cid'})


def clean(trash):
    trash = trash.replace("\n\n", " ")
    trash = trash.replace(":", "':'")
    trash = trash.replace(' ', "', '")
    return trash

cleaned = [clean(x) for x in dat]

for x in cleaned:
    print(x)

def validPassports(dat):
    import ast
    import pandas as pd
    prelim = dat

    def clean(trash):
        trash = trash.replace("\n", " ")
        trash = trash.replace(":", "':'")
        trash = trash.replace(' ', "', '")
        return trash

    prelim2 = [clean(x) for x in prelim]
    insert_quotation = lambda string: string + "'}'"
    insert_curly = lambda string: "'{'" + string
    prelim3 = [insert_quotation(x) for x in prelim2]
    prelim4 = [insert_curly(x) for x in prelim3]
    df = pd.DataFrame([ast.literal_eval(x) for x in prelim4])
    df = df.drop(columns=["cid"])
    return df.dropna(), len(df.dropna())

print(validPassports(dat[:-1]))
'''
