def day02a():
    with open("2017/day02_input.txt", 'r') as f:
        digits = [
            [int(x.strip()) for x in row.split('\t')]
            for row in f.read().strip().split('\n')
        ]
    
    checksum = 0
    for row in digits:
        checksum += max(row) - min(row)
    return checksum

def day02b():
    with open("2017/day02_input.txt", 'r') as f:
        digits = [
            [int(x.strip()) for x in row.split('\t')]
            for row in f.read().strip().split('\n')
        ]
    
    checksum = 0
    for row in digits:
        for i in range(len(row)):
            for j in range(len(row)):
                if i != j and row[j] != 0 and row[i] % row[j] == 0:
                    checksum += int(row[i] / row[j])
    return checksum

print(day02b())