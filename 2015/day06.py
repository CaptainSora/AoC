def day06a():
	with open("2015/day06_input.txt", "r") as f:
		instr = \
			f.read().replace("turn ", "").replace(",", " ").strip().split("\n")
	grid = [[False for _ in range(1000)] for _ in range(1000)]
	for line in instr:
		action, x1, y1, _, x2, y2 = line.strip().split()
		for x in range(int(x1), int(x2)+1):
			for y in range(int(y1), int(y2)+1):
				if action == "off":
					grid[x][y] = False
				elif action == "on":
					grid[x][y] = True
				else:
					grid[x][y] ^= True
	return sum([sum(line) for line in grid])

def day06b():
	with open("2015/day06_input.txt", "r") as f:
		instr = \
			f.read().replace("turn ", "").replace(",", " ").strip().split("\n")
	grid = [[0 for _ in range(1000)] for _ in range(1000)]
	for line in instr:
		action, x1, y1, _, x2, y2 = line.strip().split()
		for x in range(int(x1), int(x2)+1):
			for y in range(int(y1), int(y2)+1):
				if action == "off":
					grid[x][y] = max(0, grid[x][y] - 1)
				elif action == "on":
					grid[x][y] += 1
				else:
					grid[x][y] += 2
	return sum([sum(line) for line in grid])


print(day06a())
print(day06b())
