from math import prod

def day03a():
    with open("2020/day03_input.txt", 'r') as f:
        trees = [row.strip() for row in f.read().strip().split('\n')]
    width = len(trees[0])
    
    counter = 0
    pos = 0
    for row in trees:
        if row[pos] == '#':
            counter += 1
        pos = (pos + 3) % width
    return counter

def day03b():
    with open("2020/day03_input.txt", 'r') as f:
        trees = [row.strip() for row in f.read().strip().split('\n')]
    width = len(trees[0])
    height = len(trees)

    def treecount(right, down):
        xpos = 0
        ypos = 0
        counter = 0
        while (ypos < height):
            if trees[ypos][xpos] == '#':
                counter += 1
            ypos += down
            xpos = (xpos + right) % width
        return counter
    
    return prod([
        treecount(1, 1), treecount(3, 1), treecount(5, 1), treecount(7, 1), 
        treecount(1, 2)
    ])

print(day03b())