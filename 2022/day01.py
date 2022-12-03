def day01a():
    with open("2022/day01_input.txt") as f:
        elves = f.read().split("\n\n")
    return max([sum([int(line) for line in elf.split()]) for elf in elves])

def day01b():
    with open("2022/day01_input.txt") as f:
        elves = f.read().split("\n\n")
    return sum(sorted([
        sum([int(line) for line in elf.split()]) for elf in elves
    ])[-3:])


print(day01a())
print(day01b())