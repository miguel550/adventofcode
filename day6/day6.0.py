with open('./i.txt') as f:
    c = 0
    s = set()
    for l in f:
        s |= set(list(l.strip()))
        if l.strip() == "":
            c += len(s)
            s = set()
    c += len(s)
print(c)


