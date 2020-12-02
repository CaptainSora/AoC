def day02a():
    with open("day02_input.txt", 'r') as f:
        passwords = f.read().strip().split('\n')
        passwords = [
            line.strip().replace('-', ' ').replace(':', '').split(' ') 
            for line in passwords
        ]
    
    counter = 0
    for line in passwords:
        lower = int(line[0])
        upper = int(line[1])
        count = line[3].count(line[2])
        if lower <= count and count <= upper:
            counter += 1
    return counter

def day02b():
    with open("day02_input.txt", 'r') as f:
        passwords = f.read().strip().split('\n')
        passwords = [
            line.strip().replace('-', ' ').replace(':', '').split(' ')
            for line in passwords
        ]
    
    counter = 0
    for line in passwords:
        lower = int(line[0])-1
        upper = int(line[1])-1
        pos1 = line[3][lower] == line[2]
        pos2 = line[3][upper] == line[2]
        if (pos1 or pos2) and not (pos1 and pos2):
            counter += 1
    return counter

print(day02b())