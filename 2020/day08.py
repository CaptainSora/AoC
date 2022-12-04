from copy import deepcopy


def day08a():
    with open("2020/day08_input.txt", 'r') as f:
        instr = [
            row.strip().split(' ') 
            for row in f.read().strip().split('\n')
        ]
    
    acc = 0
    pos = 0
    visited = set()
    while True:
        if pos in visited:
            return acc
        visited.add(pos)
        if instr[pos][0] == "acc":
            acc += int(instr[pos][1])
            pos += 1
        elif instr[pos][0] == "jmp":
            pos += int(instr[pos][1])
        elif instr[pos][0] == "nop":
            pos += 1
        else:
            print("Houston we have a problem")

def day08b():
    with open("2020/day08_input.txt", 'r') as f:
        instr = [
            row.strip().split(' ') 
            for row in f.read().strip().split('\n')
        ]
    
    for i in range(len(instr)):
        if instr[i][0] == "acc":
            continue
        instr_copy = deepcopy(instr)
        if instr_copy[i][0] == "jmp":
            instr_copy[i][0] = "nop"
        elif instr_copy[i][0] == "nop":
            instr_copy[i][0] = "jmp"
        else:
            print("The eagle has not landed")
        acc = 0
        pos = 0
        visited = set()
        while True:
            if pos == len(instr_copy):
                return acc
            elif pos in visited:
                break
            visited.add(pos)
            if instr_copy[pos][0] == "acc":
                acc += int(instr_copy[pos][1])
                pos += 1
            elif instr_copy[pos][0] == "jmp":
                pos += int(instr_copy[pos][1])
            elif instr_copy[pos][0] == "nop":
                pos += 1
            else:
                print("Houston we have a problem")


print(day08a())
print(day08b())
