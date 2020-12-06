with open('./i.txt') as f:
    c = 0
    s = None
    for l in f:
        if s is None:
            s = set(list(l.strip()))
        elif l.strip() != "":
            s = s & set(list(l.strip()))
        if l.strip() == "":
            c += len(s)
            s = None
    c += len(s)
print(c)


