def pos_add(posa, posb):
    return (posa[0] + posb[0], posa[1] + posb[1])

def pos_mult(pos, scalar):
    return (pos[0] * scalar, pos[1] * scalar)

def pos_dist(pos):
    return abs(pos[0]) + abs(pos[1])

def between(value, bound1, bound2):
    # bound1 and bound2 can be in any order, but not equal
    if bound1 < bound2:
        return value >= bound1 and value <= bound2
    else:
        return value >= bound2 and value <= bound1

def cross(p1, p2, q1, q2):
    # requires p to be horizontal and q to be vertical
    # returns manhattan distance of crossing point
    if between(p1[1], q1[1], q2[1]) and between(q1[0], p1[0], p2[0]):
        return abs(q1[0]) + abs(p1[1])
    else:
        return float("inf")

def overlap(p1, p2, q1, q2):
    axis = 0
    if (p1[1] == p2[1]):
        axis = 1
    if (p1[axis] != q1[axis]):
        return float("inf")
    line1 = sorted([abs(p1[1 - axis]), abs(p2[1 - axis])])
    line2 = sorted([abs(q1[1 - axis]), abs(q2[1 - axis])])
    if line1[1] < line2[1]:
        line1, line2 = line2, line1
    # line 1 is now the further out line
    if line1[0] > line2[1]:
        return float("inf")
    return line1[0] + abs(p1[axis])

def intersect(p1, p2, q1, q2):
    p_hz = True
    q_hz = True
    if (p1[0] == p2[0]):
        p_hz = False
    if (q1[0] == q2[0]):
        q_hz = False
    
    if (p_hz or q_hz) and not (p_hz and q_hz):
        # different directions
        if p_hz:
            return cross(p1, p2, q1, q2)
        else:
            return cross(q1, q2, p1, p2)
    else:
        # same direction
        return overlap(p1, p2, q1, q2)

def day03a():
    with open("2019/day03_input.txt", 'r') as f:
        wires = [
            wire.strip().split(',')
            for wire in f.read().strip().split('\n')
        ]
    
    pos_list = [(0, 0)]
    dirs = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    for dir in wires[0]:
        step = dirs[dir[0]]
        pos_list.append(pos_add(pos_list[-1], pos_mult(step, int(dir[1:]))))
    
    w2pos = (0, 0)
    mindist = float("inf")
    for dir in wires[1]:
        step = dirs[dir[0]]
        endpoint = pos_add(w2pos, pos_mult(step, int(dir[1:])))
        for i in range(len(pos_list) - 1):
            dist = intersect(w2pos, endpoint, pos_list[i], pos_list[i+1])
            if dist > 0:
                mindist = min(mindist, dist)
        w2pos = endpoint
    
    return mindist


def pos_diff(p, q1, q2):
    # returns the sum of the distances from p to each of q1 and q2
    return (abs(p[0] - q1[0]) + abs(p[0] - q2[0])
        + abs(p[1] - q1[1]) + abs(p[1] - q2[1])
    )

def cross2(p1, p2, q1, q2):
    # requires p to be horizontal and q to be vertical
    # returns crossing point
    if between(p1[1], q1[1], q2[1]) and between(q1[0], p1[0], p2[0]):
        return [q1[0], p1[1]]
    else:
        return [0, 0]

def overlap2(p1, p2, q1, q2):
    # requires p1 and q1 to be earlier in the path
    # returns crossing point closest to p1
    axis = 0
    if (p1[1] == p2[1]):
        axis = 1
    if (p1[axis] != q1[axis]):
        return [0, 0]
    step = [0, 0]
    step[1 - axis] = 1
    if p2[1 - axis] < p1[1 - axis]:
        step[1 - axis] = -1
    if between(p1[1-axis], q1[1-axis], q2[1-axis]):
        return p1
    point = p1
    while point != p2:
        point = pos_add(point, step)
        if between(point[1-axis], q1[1-axis], q2[1-axis]):
            return point
    return [0, 0]

def intersect2(p1, p2, q1, q2):
    p_hz = True
    q_hz = True
    if (p1[0] == p2[0]):
        p_hz = False
    if (q1[0] == q2[0]):
        q_hz = False
    
    intersect = [0, 0]
    if (p_hz or q_hz) and not (p_hz and q_hz):
        # different directions
        if p_hz:
            intersect = cross2(p1, p2, q1, q2)
        else:
            intersect = cross2(q1, q2, p1, p2)
    else:
        # same direction
        intersect = overlap2(p1, p2, q1, q2)
    
    if intersect == [0, 0]:
        return float("inf")
    return pos_diff(intersect, p1, q1)

def day03b():
    with open("2019/day03_input.txt", 'r') as f:
        wires = [
            wire.strip().split(',')
            for wire in f.read().strip().split('\n')
        ]
    
    pos_list = [(0, 0)]
    dist_list = [0]
    dirs = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    for dir in wires[0]:
        step = dirs[dir[0]]
        pos_list.append(pos_add(pos_list[-1], pos_mult(step, int(dir[1:]))))
        dist_list.append(dist_list[-1] + int(dir[1:]))
    
    w2pos = (0, 0)
    w2dist = 0
    mindist = float("inf")
    for dir in wires[1]:
        step = dirs[dir[0]]
        endpoint = pos_add(w2pos, pos_mult(step, int(dir[1:])))
        for i in range(len(pos_list) - 1):
            dist = intersect2(w2pos, endpoint, pos_list[i], pos_list[i+1])
            if dist < float("inf") and dist > 0:
                mindist = min(mindist, dist_list[i] + w2dist + dist)
        w2pos = endpoint
        w2dist += int(dir[1:])
    
    return mindist

print(day03b())