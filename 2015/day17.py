from itertools import combinations


def day17a():
	with open("2015/day17_input.txt", "r") as f:
		containers = [int(c) for c in f.read().strip().split("\n")]
	return sum([
		sum(comb) == 150
		for i in range(1, len(containers) + 1)
		for comb in combinations(containers, i)
	])

def day17b():
	with open("2015/day17_input.txt", "r") as f:
		containers = [int(c) for c in f.read().strip().split("\n")]
	for i in range(1, len(containers) + 1):
		num = sum([sum(comb) == 150 for comb in combinations(containers, i)])
		if num > 0:
			return num


print(day17a())
print(day17b())
