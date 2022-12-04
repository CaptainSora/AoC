def day02a():
    with open("2019/day02_input.txt", 'r') as f:
        opcode = [int(num) for num in f.read().strip().split(',')]
    opcode[1] = 12
    opcode[2] = 2

    pos = 0
    while(opcode[pos] != 99):
        a, b, c = opcode[pos+1:pos+4]
        if opcode[pos] == 1:
            opcode[c] = opcode[a] + opcode[b]
        elif opcode[pos] == 2:
            opcode[c] = opcode[a] * opcode[b]
        else:
            print("Houston we have a problem")
            return -1
        pos += 4
    return opcode[0]

def day02b():
    with open("2019/day02_input.txt", 'r') as f:
        og_opcode = [int(num) for num in f.read().strip().split(',')]
    
    def runcode(noun, verb):
        opcode = og_opcode[:]
        opcode[1] = noun
        opcode[2] = verb

        pos = 0
        while(opcode[pos] != 99):
            a, b, c = opcode[pos+1:pos+4]
            if opcode[pos] == 1:
                opcode[c] = opcode[a] + opcode[b]
            elif opcode[pos] == 2:
                opcode[c] = opcode[a] * opcode[b]
            else:
                print("Houston we have a problem")
                return -1
            pos += 4
        return opcode[0]
    
    for a in range(100):
        for b in range(100):
            if runcode(a, b) == 19690720:
                return 100 * a + b
    print("Help")
    return -1


print(day02a())
print(day02b())
