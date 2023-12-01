from collections import Counter
from itertools import pairwise, zip_longest


def day14a():
	with open("2021/day14_input.txt", "r") as f:
		polymer, rules = f.read().strip().split("\n\n")
	ruledict = dict([tuple(line.split(" -> ")) for line in rules.split("\n")])
	for _ in range(10):
		insert = [ruledict.get("".join(pair), "") for pair in pairwise(polymer)]
		polymer = "".join(
			"".join(p) for p in zip_longest(polymer, insert, fillvalue="")
		)
	elem_count = Counter(polymer).most_common()
	return elem_count[0][1] - elem_count[-1][1]

def day14b():
	with open("2021/day14_input.txt", "r") as f:
		polymer, rules = f.read().strip().split("\n\n")
	ruledict = dict([tuple(line.split(" -> ")) for line in rules.split("\n")])
	pair_counter = Counter(["".join(pair) for pair in pairwise(polymer + "#")])
	for _ in range(40):
		new_counter = Counter()
		for pair, count in pair_counter.items():
			insert = ruledict.get(pair, "")
			if not insert:
				new_counter[pair] += count
				continue
			new_counter[pair[0] + insert] += count
			new_counter[insert + pair[1]] += count
		pair_counter = new_counter
	elems = Counter()
	for pair, count in pair_counter.items():
		elems[pair[0]] += count
	elem_count = elems.most_common()
	return elem_count[0][1] - elem_count[-1][1]


print(day14a())
print(day14b())
