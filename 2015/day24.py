from itertools import combinations
from math import prod


def day24a():
	with open("2015/day24_input.txt", "r") as f:
		packages = [int(num) for num in f.read().strip().split()][::-1]
	weight = sum(packages) // 3
	# Find minimum number of packages
	center = []
	for i in range(1, len(packages)):
		for comb in combinations(packages, i):
			if sum(comb) == weight:
				center.append(comb)
		if center:
			break
	# Return minimum QE
	return min([prod(comb) for comb in center])
	

def day24b():
	with open("2015/day24_input.txt", "r") as f:
		packages = [int(num) for num in f.read().strip().split()][::-1]
	weight = sum(packages) // 4
	# Find minimum number of packages
	center = []
	for i in range(1, len(packages)):
		for comb in combinations(packages, i):
			if sum(comb) == weight:
				center.append(comb)
		if center:
			break
	# Return minimum QE
	return min([prod(comb) for comb in center])


print(day24a())
print(day24b())
