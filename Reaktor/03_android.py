def solve():
    with open('Reaktor/03_android.txt', 'r') as f:
        strands = [[instr.split(',') for instr in line.strip().split(' ')]
            for line in f.read().strip().split('\n')]
    
    def traverse(pos, path):
        # modifies pos
        for char in path.split(','):
            if char == "D":
                pos[1] += 1
            elif char == "U":
                pos[1] -= 1
            elif char == "R":
                pos[0] += 1
            elif char == "L":
                pos[0] -= 1

    coremap = {}
    for strand in strands:
        pos = [int(num) for num in strand[0]]
        coremap[tuple(pos)] = '-'
        if len(strand) == 1:
            continue
        for char in strand[1]:
            traverse(pos, char)
            coremap[tuple(pos)] = '-'
        if strand[1][-1] in "XFS":
            coremap[tuple(pos)] = strand[1][-1]
    S = [k for k, v in coremap.items() if v == 'S'][0] # tuple
    F = [k for k, v in coremap.items() if v == 'F'][0] # tuple
    # mark paths from exit
    curdepth = [F]
    depth = 0
    found = False
    while not found:
        newdepth = []
        depth += 1
        for node in curdepth:
            for a, b in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                newnode = (node[0]+a, node[1]+b)
                if newnode not in coremap:
                    continue
                elif coremap[newnode] == "S":
                    found = True
                    break
                elif coremap[newnode] == '-':
                    newdepth.append(newnode)
                    coremap[newnode] = depth
            if found:
                break
        curdepth = newdepth
    # follow path from start
    coremap[F] = 0 # mark end as 0
    depth -= 1
    curnode = S
    path = ""
    while depth >= 0:
        for a, b in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            newnode = (curnode[0]+a, curnode[1]+b)
            if newnode in coremap and coremap[newnode] == depth:
                curnode = newnode
                step = [a, b]
                if step == [0, 1]:
                    path += "D"
                elif step == [0, -1]:
                    path += "U"
                elif step == [1, 0]:
                    path += "R"
                elif step == [-1, 0]:
                    path += "L"
                break
        depth -= 1
        if curnode == S:
            print("We have a problem")
            return -1
    return path

print(solve())