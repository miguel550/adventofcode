with open('./day2.0.txt') as f:
    valid = 0
    for line in f:
        ran, letter, p = line.split(' ')
        l, h = list(map(int, ran.split('-')))
        c = p.count(letter[0])
        if l <= c <= h:
            valid += 1

print(valid)

    
