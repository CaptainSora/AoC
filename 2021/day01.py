def day01a():
    with open("2021/day01_input.txt") as f:
        depth = [int(num) for num in f.read().strip().split("\n")]
    return sum([depth[i] - depth[i-1] > 0 for i in range(1, len(depth))])

def day01b():
    with open("2021/day01_input.txt") as f:
        depth = [int(num) for num in f.read().strip().split("\n")]
    window = [sum(depth[i-2:i+1]) for i in range(2, len(depth))]
    return sum([window[i] - window[i-1] > 0 for i in range(1, len(window))])


print(day01a())
print(day01b())