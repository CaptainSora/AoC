def day10a():
	with open("2023/day10_input.txt", "r") as f:
		tiles = f.read().strip().split("\n")
	r, c = 0, 0
	for row in range(len(tiles)):
		if "S" in tiles[row]:
			c = tiles[row].index("S")
			r = row
			break
	# [Up, Left, Down, Right]
	tiledict = {
		"|": [1, 0, 1, 0],
		"-": [0, 1, 0, 1],
		"L": [1, 0, 0, 1],
		"J": [1, 1, 0, 0],
		"7": [0, 1, 1, 0],
		"F": [0, 0, 1, 1],
		".": [0, 0, 0, 0],
		"S": [1, 1, 1, 1]
	}

	def sub(src, dir):
		return [src[i] - dir[(i + 2) % 4] for i in range(len(src))]
	
	# First step down
	steps = 1
	dir = [0, 0, 1, 0]
	r += 1
	tile = tiles[r][c]
	while tile != "S":
		dir = sub(tiledict[tile], dir)
		r += dir[2] - dir[0]
		c += dir[3] - dir[1]
		tile = tiles[r][c]
		steps += 1
	return steps // 2


def day10b():
	with open("2023/day10_input.txt", "r") as f:
		tiles = f.read().strip().split("\n")
	for row in range(len(tiles)):
		if "S" in tiles[row]:
			c = tiles[row].index("S")
			r = row
			break
	# [Up, Left, Down, Right]
	tiledict = {
		"|": [1, 0, 1, 0],
		"-": [0, 1, 0, 1],
		"L": [1, 0, 0, 1],
		"J": [1, 1, 0, 0],
		"7": [0, 1, 1, 0],
		"F": [0, 0, 1, 1],
		".": [0, 0, 0, 0],
		"S": [1, 1, 1, 1]
	}

	# Search loop and surroundings
	loop = set([(r, c)])
	cw = set()
	ccw = set()

	def sub(src, dir):
		# A rotation of +1 is counter-clockwise
		new_dir = [src[i] - dir[(i + 2) % 4] for i in range(len(src))]
		rot = new_dir.index(1) - dir.index(1)
		if rot:
			rot = (4 - rot) % 4 - 2
		return new_dir, rot
	
	# First step down
	dir = [0, 0, 1, 0]
	r += 1
	tile = tiles[r][c]
	total_rot = 0
	while tile != "S":
		loop.add((r, c))
		j = dir.index(1)
		dir, rot = sub(tiledict[tile], dir)
		total_rot += rot
		neighbours = [
			(r, c+1), (r-1, c), (r, c-1), (r+1, c),
			(r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1)
		]
		i = dir.index(1)
		# Add either side of the loop
		cw.add(neighbours[i])
		ccw.add(neighbours[(i+2)%4])
		cw.add(neighbours[j])
		ccw.add(neighbours[(j+2)%4])
		# Step
		r += dir[2] - dir[0]
		c += dir[3] - dir[1]
		tile = tiles[r][c]
	
	# Select correct side
	adj = cw if total_rot < 0 else ccw
	inside = set()

	def valid(r, c):
		return 0 <= r < len(tiles) and 0 <= c < len(tiles[0])
	
	while adj:
		r, c = adj.pop()
		if not valid(r, c) or (r, c) in inside or (r, c) in loop:
			continue
		inside.add((r, c))
		neighbours = [(r, c+1), (r+1, c), (r, c-1), (r-1, c)]
		for n in neighbours:
			if valid(*n) and n not in loop and n not in adj and n not in inside:
				adj.add(n)
	
	return len(inside)


print(day10a())
print(day10b())
