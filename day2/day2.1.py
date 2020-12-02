with open('./day2.0.txt') as f:
    valid = 0
    for line in f:
        ran, letter, p = line.split(' ')
        l, h = list(map(int, ran.split('-')))
        if (p[l-1] == letter[0] or p[h-1] == letter[0]) and p[l-1] != p[h-1]:
            valid += 1

print(valid)

    
