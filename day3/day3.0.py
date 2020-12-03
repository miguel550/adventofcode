with open('./day3.0.txt') as f:
    trees = 0
    curr_col = 0
    for i, l in enumerate(f):
        if i == 0:
            continue
        curr_col = (3 + curr_col) % len(l.strip())
        if l[curr_col] == '#':
            trees += 1

print(trees)


