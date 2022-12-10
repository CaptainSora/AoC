from itertools import combinations

def day21a():
	with open("2015/day21_input.txt", "r") as f:
		bhp, batk, bdef = [int(num) for num in f.read().split()[2::2]]
	weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
	armor = [
		[0, 0, 0], [13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]
	]
	rings = [
		[25, 1, 0], [50, 2, 0], [100, 3, 0],
		[20, 0, 1], [40, 0, 2], [80, 0, 3]
	]
	rings = list(combinations(rings, 2)) + list(combinations(rings, 1)) + [[]]
	loadouts = []
	for wep in weapons:
		for arm in armor:
			for r in rings:
				equip = [wep] + [arm]
				equip.extend(r)
				loadouts.append([sum(stat) for stat in list(zip(*equip))])
	loadouts.sort()
	for l in loadouts:
		hp = 100
		bosshp = bhp
		while hp > 0:
			bosshp -= max(1, l[1] - bdef)
			if bosshp <= 0:
				return l[0]
			hp -= max(1, batk - l[2])

def day21b():
	with open("2015/day21_input.txt", "r") as f:
		bhp, batk, bdef = [int(num) for num in f.read().split()[2::2]]
	weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
	armor = [
		[0, 0, 0], [13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]
	]
	rings = [
		[25, 1, 0], [50, 2, 0], [100, 3, 0],
		[20, 0, 1], [40, 0, 2], [80, 0, 3]
	]
	rings = list(combinations(rings, 2)) + list(combinations(rings, 1)) + [[]]
	loadouts = []
	for wep in weapons:
		for arm in armor:
			for r in rings:
				equip = [wep] + [arm]
				equip.extend(r)
				loadouts.append([sum(stat) for stat in list(zip(*equip))])
	loadouts.sort(reverse=True)
	for l in loadouts:
		hp = 100
		bosshp = bhp
		while bosshp > 0:
			bosshp -= max(1, l[1] - bdef)
			if hp <= 0:
				return l[0]
			hp -= max(1, batk - l[2])


print(day21a())
print(day21b())
