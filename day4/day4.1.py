import re
with open('./day4.0.txt') as f:
    c = 0
    valid = 0
    for l in f:
        if 'byr:' in l:
            m = re.search(r'byr:(\d{4})\W', l)
            if m and 1920 <= int(m.groups()[0]) <= 2002:
                valid +=1
        if 'iyr:' in l:
            m = re.search(r'iyr:(\d{4})\W', l)
            if m and 2010 <= int(m.groups()[0]) <= 2020:
                valid +=1
        if 'eyr:' in l:
            m = re.search(r'eyr:(\d{4})\W', l)
            if m and 2020 <= int(m.groups()[0]) <= 2030:
                valid +=1
        if 'hgt:' in l:
            m = re.search(r'hgt:(\d+)(cm|in)\W', l)
            if m:
                if m.groups()[1] == "cm":
                    if 150 <= int(m.groups()[0]) <= 193:
                        valid +=1
                else:
                    if 59 <= int(m.groups()[0]) <= 76:
                        valid +=1
        if 'hcl:' in l:
            m = re.search(r'hcl:#[a-f0-9]{6}\W', l)
            if m:
                valid +=1
        if 'ecl:' in l:
            a = [
                'amb',
                'blu',
                'brn',
                'gry',
                'grn',
                'hzl',
                'oth'
            ]
            for i in a:
                if 'ecl:' + i in l:
                    valid +=1
                    break
        if 'pid:' in l:
            m = re.search(r'pid:(\d{9})\W', l)
            if m:
                valid +=1
        if l.strip() == "":
            if valid == 7:
                c += 1
            valid = 0

# print(valid)
if valid == 7:
    c += 1
print(c)
