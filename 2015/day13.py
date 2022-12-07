from itertools import permutations


def day13a():
	with open("2015/day13_input.txt", "r") as f:
		prefs = [l.split() for l in f.read().strip().split("\n")]
	names = list(set(list(zip(*prefs))[0]))
	pmatrix = [[0 for _ in names] for _ in names]
	for line in prefs:
		amt = int(line[3])
		if line[2] == "lose":
			amt *= -1
		pmatrix[names.index(line[0])][names.index(line[-1][:-1])] = amt
	happiness = 0
	for perm in permutations(range(len(names))):
		order = list(perm) + [perm[0]]
		happiness = max(happiness, sum([
			pmatrix[order[i-1]][order[i]] + pmatrix[order[i]][order[i-1]]
			for i in range(1, len(order))
		]))
	return happiness

def day13b():
	with open("2015/day13_input.txt", "r") as f:
		prefs = [l.split() for l in f.read().strip().split("\n")]
	names = list(set(list(zip(*prefs))[0]))
	names.append("Me")
	pmatrix = [[0 for _ in names] for _ in names]
	for line in prefs:
		amt = int(line[3])
		if line[2] == "lose":
			amt *= -1
		pmatrix[names.index(line[0])][names.index(line[-1][:-1])] = amt
	happiness = 0
	for perm in permutations(range(len(names))):
		order = list(perm) + [perm[0]]
		happiness = max(happiness, sum([
			pmatrix[order[i-1]][order[i]] + pmatrix[order[i]][order[i-1]]
			for i in range(1, len(order))
		]))
	return happiness


print(day13a())
print(day13b())
