def day03a():
    with open("2018/day03_input.txt", 'r') as f:
        boxes = [
            [
                int(x) for x in
                claim.strip().split('@ ')[1].replace(',', ' ').\
                    replace(':', '').replace('x', ' ').split(' ')
            ]
            for claim in f.read().strip().split('\n')
        ]
    
    size = max([max(row[0] + row[2], row[1] + row[3]) for row in boxes])
    fabric = [0] * (size**2)
    for claim in boxes:
        for i in range(claim[3]): # height
            for j in range(claim[2]): # width
                fabric[size * (claim[1] + i) + (claim[0] + j)] += 1
    return sum([x >= 2 for x in fabric])

def day03b():
    with open("2018/day03_input.txt", 'r') as f:
        boxes = [
            [
                int(x) for x in
                claim.strip().replace('#', '').replace('@ ', '')\
                    .replace(',', ' ').replace(':', '').replace('x', ' ')\
                    .split(' ')
            ]
            for claim in f.read().strip().split('\n')
        ]
    
    size = max([max(row[1] + row[3], row[2] + row[4]) for row in boxes])
    fabric = [set() for _ in range(size**2)]
    uniq = set()
    for claim in boxes:
        solo = True
        for i in range(claim[4]): # height
            for j in range(claim[3]): # width
                if len(fabric[size * (claim[2]+i) + (claim[1]+j)]) > 0:
                    solo = False
                    uniq -= fabric[size * (claim[2]+i) + (claim[1]+j)]
                fabric[size * (claim[2]+i) + (claim[1]+j)].add(claim[0])
        if solo:
            uniq.add(claim[0])
    return list(uniq)[0]


print(day03a())
print(day03b())
