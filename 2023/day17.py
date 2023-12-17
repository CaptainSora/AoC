from heapq import heapify, heappop, heappush


def day17a():
	with open("2023/day17_input.txt", "r") as f:
		city = [
			[int(num) for num in row]
			for row in f.read().strip().split("\n")
		]
	rmax, cmax = len(city) - 1, len(city[0]) - 1
	# State tuple: heat_loss, row, col, up, down, left, right
	frontier = [(0, 0, 0, 0, 0, 0, 0)]
	heapify(frontier)
	visited = set()
	while frontier:
		node = heappop(frontier)
		heat, *key = node
		if tuple(key) in visited:
			continue
		visited.add(tuple(key))
		row, col, u, d, l, r = key
		if row == rmax and col == cmax:
			return heat
		# Up
		if row > 0 and 0 <= u < 3:
			heappush(
				frontier,
				(heat + city[row-1][col], row - 1, col, u+1, -1, 0, 0)
			)
		# Down
		if row < rmax and 0 <= d < 3:
			heappush(
				frontier,
				(heat + city[row+1][col], row + 1, col, -1, d+1, 0, 0)
			)
		# Left
		if col > 0 and 0 <= l < 3:
			heappush(
				frontier,
				(heat + city[row][col-1], row, col - 1, 0, 0, l+1, -1)
			)
		# Right
		if col < cmax and 0 <= r < 3:
			heappush(
				frontier,
				(heat + city[row][col+1], row, col + 1, 0, 0, -1, r+1)
			)


def day17b():
	with open("2023/day17_input.txt", "r") as f:
		city = [
			[int(num) for num in row]
			for row in f.read().strip().split("\n")
		]
	rmax, cmax = len(city) - 1, len(city[0]) - 1
	# State tuple: heat_loss, row, col, up, down, left, right
	frontier = [(0, 0, 0, 0, 0, 0, 0)]
	heapify(frontier)
	visited = set()
	while frontier:
		node = heappop(frontier)
		heat, *key = node
		if tuple(key) in visited:
			continue
		visited.add(tuple(key))
		row, col, u, d, l, r = key
		dmax = max(u, d, l, r)
		if row == rmax and col == cmax and dmax >= 4:
			return heat
		# Up
		if row > 0 and 0 <= u < 10 and (u == dmax or dmax >= 4):
			heappush(
				frontier,
				(heat + city[row-1][col], row - 1, col, u+1, -1, 0, 0)
			)
		# Down
		if row < rmax and 0 <= d < 10 and (d == dmax or dmax >= 4):
			heappush(
				frontier,
				(heat + city[row+1][col], row + 1, col, -1, d+1, 0, 0)
			)
		# Left
		if col > 0 and 0 <= l < 10 and (l == dmax or dmax >= 4):
			heappush(
				frontier,
				(heat + city[row][col-1], row, col - 1, 0, 0, l+1, -1)
			)
		# Right
		if col < cmax and 0 <= r < 10 and (r == dmax or dmax >= 4):
			heappush(
				frontier,
				(heat + city[row][col+1], row, col + 1, 0, 0, -1, r+1)
			)


print(day17a())
print(day17b())
