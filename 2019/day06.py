def day06a():
    with open("2019/day06_input.txt", 'r') as f:
        orbits = [
            pair.strip().split(')') 
            for pair in f.read().strip().split('\n')
        ]
    
    orbit_dict = {'COM': 0}
    pos = 0
    while orbits:
        while orbits[pos][0] not in orbit_dict:
            pos += 1
        orbit_dict[orbits[pos][1]] = orbit_dict[orbits[pos][0]] + 1
        orbits.pop(pos)
        pos = 0
    
    return sum(orbit_dict.values())

def day06b():
    with open("2019/day06_input.txt", 'r') as f:
        orbits = [
            pair.strip().split(')') 
            for pair in f.read().strip().split('\n')
        ]
    
    santa_path = ['SAN']
    while santa_path[-1] != 'COM':
        for pair in orbits:
            if pair[1] == santa_path[-1]:
                santa_path.append(pair[0])
                break
    down_transfers = -1
    cur_pos = 'YOU'
    while cur_pos not in santa_path:
        for pair in orbits:
            if pair[1] == cur_pos:
                down_transfers += 1
                cur_pos = pair[0]
                break
    return down_transfers + santa_path.index(cur_pos) - 1


print(day06a())
print(day06b())
