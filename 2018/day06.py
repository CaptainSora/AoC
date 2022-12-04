def pos_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def day06a():
    with open("2018/day06_input.txt", 'r') as f:
        points = [
            [int(x) for x in row.strip().split(', ')]
            for row in f.read().strip().split('\n')
        ]
    
    size = max([max(p[0], p[1]) for p in points])
    grid = [0] * (size ** 2)
    boundary = set()
    for i in range(size):
        for j in range(size):
            mindist = float('inf')
            closest = []
            for k in range(len(points)):
                d = pos_dist([i, j], points[k])
                if d < mindist:
                    closest = [k]
                    mindist = d
                elif d == mindist:
                    closest.append(k)
            if len(closest) > 1:
                grid[i * size + j] = -1
            else:
                grid[i * size + j] = closest[0]
                if i == 0 or i+1 == size or j == 0 or j+1 == size:
                    boundary.add(closest[0])
    maxarea = 0
    for a in range(len(points)):
        if a not in boundary:
            area = grid.count(a)
            maxarea = max(maxarea, area)
    return maxarea

def day06b():
    with open("2018/day06_input.txt", 'r') as f:
        points = [
            [int(x) for x in row.strip().split(', ')]
            for row in f.read().strip().split('\n')
        ]
    
    size = max([max(p[0], p[1]) for p in points])
    counter = 0
    for i in range(size):
        for j in range(size):
            totaldist = 0
            for k in range(len(points)):
                totaldist += pos_dist([i, j], points[k])
            if totaldist < 10000:
                counter += 1
    return counter


print(day06a())
print(day06b())
