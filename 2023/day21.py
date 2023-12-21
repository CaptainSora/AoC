from itertools import count, pairwise


def day21a():
	with open("2023/day21_input.txt", "r") as f:
		grid = f.read().strip().split("\n")
	rocks = set()
	reach = {}
	frontier = []
	# Load start and rocks
	for r, row in enumerate(grid):
		for c, tile in enumerate(row):
			if tile == "S":
				frontier.append((r, c))
			elif tile == "#":
				rocks.add((r, c))
	# Add start
	reach[frontier[0]] = 0

	def valid(r, c):
		return 0 <= r < len(grid) and 0 <= c < len(grid[0])
	
	# Search
	for i in range(1, 65):
		next = []
		for r, c in frontier:
			neighbours = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
			for n in neighbours:
				if valid(*n) and n not in rocks and n not in reach:
					next.append(n)
					reach[n] = i
		frontier = next
	
	return len([v for v in reach.values() if v % 2 == 0])


def day21b_old():
	"""
	Abandoned first draft. Was close but too many edge cases.
	Didn't notice starting row/column was open, it's probably wrong anyway.
	"""
	with open("2023/day21_input.txt", "r") as f:
		grid = f.read().strip().split("\n")
	# Square grid
	sidelen = len(grid)
	total_steps = 26501365
	rocks = set()
	# w, x, y, z are the four corners
	reach = {"S": {}, "w": {}, "x": {}, "y": {}, "z": {}}
	start = None
	# Load start and rocks
	for r, row in enumerate(grid):
		for c, tile in enumerate(row):
			if tile == "S":
				start = (r, c)
			elif tile == "#":
				rocks.add((r, c))

	def valid(r, c):
		return 0 <= r < sidelen and 0 <= c < sidelen

	starts = {
		"S": start, "w": (0, 0), "x": (0, sidelen - 1),
		"y": (sidelen - 1, 0), "z": (sidelen - 1, sidelen - 1)
	}

	# Search from each starting location
	for origin, pos in starts.items():
		reach[origin][pos] = 0
		frontier = [pos]
		for i in count(1):
			if not frontier:
				break
			next = []
			for r, c in frontier:
				neighbours = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
				for n in neighbours:
					if valid(*n) and n not in rocks and n not in reach[origin]:
						next.append(n)
						reach[origin][n] = i
			frontier = next
	
	# 130 steps from start to any corner
	tile_step = 130
	ntiles, new_steps = divmod((total_steps - tile_step), sidelen)
	# Therefore, each subsequent tile is opposite parity
	# Note! Looking for odd steps
	even_reach = [v % 2 == total_steps % 2 for v in reach["S"].values()]
	# Starting tile is an even tile (index 0)
	tile_reach = [sum(even_reach), len(even_reach) - sum(even_reach)]

	# Compute plots reached in complete tiles
	total_tiles = 2 * ntiles * (ntiles + 1) + 1
	k = (ntiles - 1) // 2
	even_tiles = 4 * k * (k + 1) + 1
	odd_tiles = total_tiles - even_tiles
	total_plots = even_tiles * tile_reach[0] + odd_tiles * tile_reach[1]

	# Compute plots reached in incomplete tiles
	# 1. Orthogonal tiles
	parity = (new_steps - 1) % 2
	for a, b in pairwise("wxzyw"):
		pair_reach = {k: min(reach[a][k], reach[b][k]) for k in reach[a]}
		total_plots += len([
			n % 2 == parity
			for n in pair_reach.values()
			if n <= new_steps - 1
		])
	# 2. Diagonal tiles (inner layer)
	parity = (new_steps - 2) % 2
	for a in "wxyz":
		total_plots += ntiles * len([
			n % 2 == parity
			for n in reach[a].values()
			if n <= new_steps - 2 + tile_step
		])
	# 3. Diagonal tiles (outer layer)
	for a in "wxyz":
		total_plots += (ntiles + 1) * len([
			n % 2 == parity
			for n in reach[a].values()
			if n <= new_steps - 2 + tile_step
		])
	
	return total_plots

def day21b():
	"""
	Needed hint for quadratic relation existing.
	"""
	with open("2023/day21_input.txt", "r") as f:
		grid = f.read().replace("S", ".").strip().split("\n")
	start = (65 + 131 * 2, 65 + 131 * 2)
	repgrid = [grid[i % len(grid)] * 5 for i in range(5 * len(grid))]

	# Find first three terms of quadratic
	reach = {}
	reach[start] = 0
	frontier = [start]
	terms = []
	for i in range(1, start[0] + 1):
		next = []
		for r, c in frontier:
			neighbours = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
			for n in neighbours:
				if repgrid[n[0]][n[1]] == "." and n not in reach:
					next.append(n)
					reach[n] = i
		frontier = next
		# Record steps
		if i % 131 == 65:
			terms.append(len([v for v in reach.values() if v % 2 == i % 2]))
	
	# Compute quadratic
	c, y, z = terms
	a = (z - 2 * y + c) // 2
	b = (4 * y - z - 3 * c) // 2
	n, _ = divmod(26501365, len(grid))

	return a * n * n + b * n + c


print(day21a())
print(day21b())
