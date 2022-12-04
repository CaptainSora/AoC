def day04a():
    with open("2022/day04_input.txt") as f:
        pairs = [
            [int(num) for num in line.replace("-", ",").split(",")]
            for line in f.read().strip().split("\n")
        ]
    return sum([(p[0] - p[2]) * (p[1] - p[3]) <= 0 for p in pairs])

def day04b():
    with open("2022/day04_input.txt") as f:
        pairs = [
            [int(num) for num in line.replace("-", ",").split(",")]
            for line in f.read().strip().split("\n")
        ]
    return sum([(p[1] - p[2]) * (p[0] - p[3]) <= 0 for p in pairs])


print(day04a())
print(day04b())