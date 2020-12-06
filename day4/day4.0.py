with open('./day4.0.txt') as f:
    c = 0
    valid = 0
    for l in f:
        if 'byr:' in l:
            valid +=1
        if 'iyr:' in l:
            valid +=1
        if 'eyr:' in l:
            valid +=1
        if 'hgt:' in l:
            valid +=1
        if 'hcl:' in l:
            valid +=1
        if 'ecl:' in l:
            valid +=1
        if 'pid:' in l:
            valid +=1
        if l.strip() == "":
            # print(valid)
            if valid == 7:
                c += 1
            valid = 0

# print(valid)
if valid == 7:
    c += 1
print(c)
