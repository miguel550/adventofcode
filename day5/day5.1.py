s = {i for i in range(0, 1024)}
with open('./input.txt') as f:
    for code in f:
        l = 0
        h = 127
        r = None
        col = None

        for c in code[:6]:
            if c == 'F':
                h = (l + h)//2
            elif c == 'B':
                l = (l + h + 1)//2

        if code[6] == 'F':
            r = l
        else:
            r = h
                
        ch = 7
        cl = 0
        for c in code[7:-1]:
            if c == 'L':
                ch = (cl + ch)//2
            elif c == 'R':
                cl = (cl + ch + 1)//2
        if code[-1] == 'L':
            col = cl
        else:
            col = ch

        s -= set([r * 8 + col])

print(s)


