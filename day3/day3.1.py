with open('./day3.0.txt') as f:
    trees_1 = 0
    trees_3 = 0
    trees_5 = 0
    trees_7 = 0
    trees_12 = 0

    curr_col_1 = 0
    curr_col_3 = 0
    curr_col_5 = 0
    curr_col_7 = 0
    curr_col_12 = 0

    for i, l in enumerate(f):

        if i == 0:
            continue

        if i % 2 == 0:
            curr_col_12 = (1 + curr_col_12) % len(l.strip)
            if l[curr_col_12] == '#':
                trees_12 += 1

        curr_col_1 = (1 + curr_col_1) % len(l.strip())
        curr_col_3 = (3 + curr_col_3) % len(l.strip())
        curr_col_5 = (5 + curr_col_5) % len(l.strip())
        curr_col_7 = (7 + curr_col_7) % len(l.strip())

        if l[curr_col_1] == '#':
            trees_1 += 1

        if l[curr_col_3] == '#':
            trees_3 += 1

        if l[curr_col_5] == '#':
            trees_5 += 1

        if l[curr_col_7] == '#':
            trees_7 += 1

print(trees_1 * trees_3 * trees_5 * trees_7 * trees_12)


