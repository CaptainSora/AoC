def day05a():
    with open("2019/day05_input.txt", 'r') as f:
        opcode = [int(num) for num in f.read().strip().split(',')]

    input = 1
    pos = 0
    while(str(opcode[pos])[-2:] != "99"):
        a, b, c = opcode[pos+1:pos+4]
        instr = f'{opcode[pos]:05}'
        if instr[-2:] == '01':
            a, b, c = opcode[pos+1:pos+4]
            if instr[2] == '0':
                a = opcode[a]
            if instr[1] == '0':
                b = opcode[b]
            opcode[c] = a + b
            pos += 4
        elif instr[-2:] == '02':
            a, b, c = opcode[pos+1:pos+4]
            if instr[2] == '0':
                a = opcode[a]
            if instr[1] == '0':
                b = opcode[b]
            opcode[c] = a * b
            pos += 4
        elif instr[-2:] == '03':
            a = opcode[pos+1]
            opcode[a] = input
            pos += 2
        elif instr[-2:] == '04':
            a = opcode[pos+1]
            if instr[2] == '0':
                a = opcode[a]
            print(a)
            pos += 2
        else:
            print("Houston we have a problem")
            return -1

def day05b():
    with open("2019/day05_input.txt", 'r') as f:
        opcode = [int(num) for num in f.read().strip().split(',')]

    input = 5
    pos = 0
    while(str(opcode[pos])[-2:] != "99"):
        instr = f'{opcode[pos]:05}'
        if instr[-2:] == '01':
            a, b, c = opcode[pos+1:pos+4]
            if instr[2] == '0':
                a = opcode[a]
            if instr[1] == '0':
                b = opcode[b]
            opcode[c] = a + b
            pos += 4
        elif instr[-2:] == '02':
            a, b, c = opcode[pos+1:pos+4]
            if instr[2] == '0':
                a = opcode[a]
            if instr[1] == '0':
                b = opcode[b]
            opcode[c] = a * b
            pos += 4
        elif instr[-2:] == '03':
            a = opcode[pos+1]
            opcode[a] = input
            pos += 2
        elif instr[-2:] == '04':
            a = opcode[pos+1]
            if instr[2] == '0':
                a = opcode[a]
            print(a)
            pos += 2
        elif instr[-2:] == '05':
            a, b = opcode[pos+1:pos+3]
            if instr[2] == '0':
                a = opcode[a]
            if instr[1] == '0':
                b = opcode[b]
            if a != 0:
                pos = b
            else:
                pos += 3
        elif instr[-2:] == '06':
            a, b = opcode[pos+1:pos+3]
            if instr[2] == '0':
                a = opcode[a]
            if instr[1] == '0':
                b = opcode[b]
            if a == 0:
                pos = b
            else:
                pos += 3
        elif instr[-2:] == '07':
            a, b, c = opcode[pos+1:pos+4]
            if instr[2] == '0':
                a = opcode[a]
            if instr[1] == '0':
                b = opcode[b]
            opcode[c] = int(a < b)
            pos += 4
        elif instr[-2:] == '08':
            a, b, c = opcode[pos+1:pos+4]
            if instr[2] == '0':
                a = opcode[a]
            if instr[1] == '0':
                b = opcode[b]
            opcode[c] = int(a == b)
            pos += 4
        else:
            print("Houston we have a problem")
            return -1


day05a()
day05b()
