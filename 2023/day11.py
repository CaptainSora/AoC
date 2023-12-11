from itertools import combinations


def day11a():
	with open("2023/day11_input.txt", "r") as f:
		gal_map = f.read().strip().split("\n")
	gal_map_t = ["".join(col) for col in zip(*gal_map)]
	empty_rows = [
		i for i in range(len(gal_map))
		if gal_map[i].find("#") == -1
	]
	empty_cols = [
		i for i in range(len(gal_map_t))
		if gal_map_t[i].find("#") == -1
	]
	galaxies = []
	for r, row in enumerate(gal_map):
		for c, char in enumerate(row):
			if char == "#":
				galaxies.append((r, c))
	
	def dist(g1, g2):
		r1, c1 = min(g1[0], g2[0]), min(g1[1], g2[1])
		r2, c2 = max(g1[0], g2[0]), max(g1[1], g2[1])
		dr = r2 - r1 + len([r for r in empty_rows if r1 < r < r2])
		dc = c2 - c1 + len([c for c in empty_cols if c1 < c < c2])
		return dr + dc
	
	total_dist = 0
	for g1, g2 in combinations(galaxies, r=2):
		total_dist += dist(g1, g2)
	
	return total_dist


def day11b():
	with open("2023/day11_input.txt", "r") as f:
		gal_map = f.read().strip().split("\n")
	gal_map_t = ["".join(col) for col in zip(*gal_map)]
	empty_rows = [
		i for i in range(len(gal_map))
		if gal_map[i].find("#") == -1
	]
	empty_cols = [
		i for i in range(len(gal_map_t))
		if gal_map_t[i].find("#") == -1
	]
	galaxies = []
	for r, row in enumerate(gal_map):
		for c, char in enumerate(row):
			if char == "#":
				galaxies.append((r, c))
	
	def dist(g1, g2, exp=10**6-1):
		r1, c1 = min(g1[0], g2[0]), min(g1[1], g2[1])
		r2, c2 = max(g1[0], g2[0]), max(g1[1], g2[1])
		dr = r2 - r1 + exp * len([r for r in empty_rows if r1 < r < r2])
		dc = c2 - c1 + exp * len([c for c in empty_cols if c1 < c < c2])
		return dr + dc
	
	total_dist = 0
	for g1, g2 in combinations(galaxies, r=2):
		total_dist += dist(g1, g2)
	
	return total_dist


print(day11a())
print(day11b())
