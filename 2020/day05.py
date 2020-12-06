def day05a():
    with open("2020/day05_input.txt", 'r') as f:
        passes = [row.strip() for row in f.read().strip().split('\n')]
    
    highest = 0
    for p in passes:
        row = 0
        col = 0
        for i in range(7):
            if p[i] == 'B':
                row += 2**(6-i)
        for j in range(3):
            if p[7+j] == 'R':
                col += 2**(2-j)
        highest = max(highest, 8 * row + col)
    return highest

def day05b():
    with open("2020/day05_input.txt", 'r') as f:
        passes = [row.strip() for row in f.read().strip().split('\n')]
    
    seats = []
    for p in passes:
        row = 0
        col = 0
        for i in range(7):
            if p[i] == 'B':
                row += 2**(6-i)
        for j in range(3):
            if p[7+j] == 'R':
                col += 2**(2-j)
        seats.append(8 * row + col)
    return min([x+1 for x in seats if x+1 not in seats])

print(day05b())