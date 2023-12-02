from heapq import heappop, heappush


def day15a():
	with open("2021/day15_input.txt", "r") as f:
		risk = [[int(d) for d in line] for line in f.read().strip().split("\n")]
	total_risk = [[0 for _ in range(len(risk))] for _ in range(len(risk))]
	# Assuming only down and right moves
	for dist in range(1, len(risk) * 2 - 1):
		for x in range(max(0, dist - len(risk) + 1), min(dist + 1, len(risk))):
			y = dist - x
			prev = []
			if y > 0:
				prev.append(total_risk[x][y-1])
			if x > 0:
				prev.append(total_risk[x-1][y])
			total_risk[x][y] = risk[x][y] + min(prev)
	return total_risk[-1][-1]


def day15b():
	with open("2021/day15_input.txt", "r") as f:
		risk = [[int(d) for d in line] for line in f.read().strip().split("\n")]
	sidelen = 5 * len(risk)

	def get_risk(x, y):
		nonlocal risk
		qx, rx = divmod(x, len(risk))
		qy, ry = divmod(y, len(risk))
		return (risk[rx][ry] + qx + qy - 1) % 9 + 1

	# Dijkstra
	frontier = [(0, (0, 0))]
	goal = (sidelen - 1, sidelen - 1)
	visited = set()
	while frontier:
		cost, loc = heappop(frontier)
		if loc == goal:
			return cost
		if loc in visited:
			continue
		step = [
			pos for pos in [
				(loc[0] + 1, loc[1]), (loc[0] - 1, loc[1]),
				(loc[0], loc[1] + 1), (loc[0], loc[1] - 1)
			]
			if pos not in visited
			and 0 <= pos[0] < sidelen
			and 0 <= pos[1] < sidelen
		]
		for pos in step:
			heappush(frontier, (get_risk(*pos) + cost, pos))
		visited.add(loc)
		

print(day15a())
print(day15b())
