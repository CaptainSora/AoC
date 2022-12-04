def day01a():
    with open("2020/day01_input.txt", 'r') as f:
        entries = [int(num.strip()) for num in f.read().split()]

    for num in entries:
        if (2020 - num) in entries:
            return num * (2020 - num)

def day01b():
    with open("2020/day01_input.txt", 'r') as f:
        entries = [int(num.strip()) for num in f.read().split()]

    for a in range(len(entries)):
        for b in range(a+1, len(entries)):
            for c in range(b+1, len(entries)):
                if entries[a] + entries[b] + entries[c] == 2020:
                    return entries[a] * entries[b] * entries[c]


print(day01a())
print(day01b())
            