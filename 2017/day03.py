def day03a():
    target = 325489
    i = 3
    while i**2 < target:
        i += 2
    value = i ** 2
    pos = [int((i-1)/2), -1 * int((i-1)/2)]
    while value > target and abs(pos[0]) <= abs(pos[1]):
        pos[0] -= 1
        value -= 1
    return abs(pos[0]) + abs(pos[1])

def day03b():
    target = 325489
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    size = 20
    grid = [[0] * size for _ in range(size)]
    pos = [int(size / 2), int(size / 2)]
    grid[pos[1]][pos[0]] = 1
    def sumadj(pos):
        x = pos[0]
        y = pos[1]
        return (
            grid[y][x+1] + grid[y+1][x+1] + grid[y+1][x] + grid[y+1][x-1] +
            grid[y][x-1] + grid[y-1][x-1] + grid[y-1][x] + grid[y-1][x+1]
        )
    
    def iszero(pos, dir):
        newpos = [pos[0] + dir[0], pos[1] + dir[1]]
        return grid[newpos[1]][newpos[0]] == 0
    
    value = 1
    dir_index = 0
    while value < target:
        if iszero(pos, dirs[(dir_index + 1) % 4]):
            dir_index = (dir_index + 1) % 4
        dir = dirs[dir_index]
        pos[0] += dir[0]
        pos[1] += dir[1]
        value = sumadj(pos)
        grid[pos[1]][pos[0]] = value
    return value


print(day03a())
print(day03b())
