def day05a():
    with open("2018/day05_input.txt", 'r') as f:
        compound = f.read().strip()
    
    pos = 1
    while pos < len(compound):
        if compound[pos-1] == compound[pos].swapcase():
            compound = compound[:pos-1] + compound[pos+1:]
            pos -= 1
        else:
            pos += 1
    return len(compound)

def day05b():
    with open("2018/day05_input.txt", 'r') as f:
        compound = f.read().strip()
    
    minlength = float("inf")
    for l in "abcdefghijklmnopqrstuvwxyz":
        new_cmp = compound.replace(l, '').replace(l.swapcase(), '')
        pos = 1
        while pos < len(new_cmp):
            if new_cmp[pos-1] == new_cmp[pos].swapcase():
                new_cmp = new_cmp[:pos-1] + new_cmp[pos+1:]
                pos -= 1
            else:
                pos += 1
        minlength = min(minlength, len(new_cmp))
    return minlength

print(day05b())