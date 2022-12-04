from itertools import permutations

def intcode(opcode, inputarray):
    # opcode must be a list of numbers
    input_index = 0
    output = 0
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
            opcode[a] = inputarray[input_index]
            input_index += 1
            pos += 2
        elif instr[-2:] == '04':
            a = opcode[pos+1]
            if instr[2] == '0':
                a = opcode[a]
            output = a
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

    return output

def day07a():
    with open("2019/day07_input.txt", 'r') as f:
        opcode = [int(num) for num in f.read().strip().split(',')]
    
    maxoutput = 0
    for phase in permutations([0, 1, 2, 3, 4], 5):
        a_out = intcode(opcode[:], [phase[0], 0])
        b_out = intcode(opcode[:], [phase[1], a_out])
        c_out = intcode(opcode[:], [phase[2], b_out])
        d_out = intcode(opcode[:], [phase[3], c_out])
        e_out = intcode(opcode[:], [phase[4], d_out])
        maxoutput = max(maxoutput, e_out)
    return maxoutput

def intcode_state(state):
    # state = (opcode, inputarray, pos)
    # opcode must be a list of numbers
    # returns updated state, with imputarray replaced with output
    opcode = state[0]
    inputarray = state[1]
    pos = state[2]
    input_index = 0
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
            opcode[a] = inputarray[input_index]
            input_index += 1
            pos += 2
        elif instr[-2:] == '04':
            a = opcode[pos+1]
            if instr[2] == '0':
                a = opcode[a]
            pos += 2
            return [opcode, a, pos] # OUTPUT
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
    return [opcode, -1, -1]

def day07b():
    with open("2019/day07_input.txt", 'r') as f:
        opcode = [int(num) for num in f.read().strip().split(',')]
    
    max_final_output = 0
    for phase in permutations([5, 6, 7, 8, 9], 5):
        opcodes = [opcode[:] for _ in range(5)]
        posns = [0 for _ in range(5)]
        init = [False for _ in range(5)]
        output = 0
        last_out = 0
        amp = 0 # Which amplifier is executing
        while True:
            inputarray = [output]
            if not init[amp]:
                init[amp] = True
                inputarray = [phase[amp], output]
            retval = intcode_state([
                opcodes[amp],
                inputarray,
                posns[amp]
            ])
            opcodes[amp] = retval[0]
            if retval[1] == -1:
                break
            output = retval[1]
            if amp == 4:
                last_out = retval[1]
            posns[amp] = retval[2]
            amp = (amp + 1) % 5
        max_final_output = max(max_final_output, last_out)
    return max_final_output


print(day07a())
print(day07b())
    