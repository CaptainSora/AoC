def day24a():
	with open("2020/day24_input.txt", "r") as f:
		instr = f.read().strip().split('\n')
	black = set()
	dirs = {
		"ne": [0, 1], "nw": [-1, 1], "w": [-1, 0],
		"sw": [0, -1], "se": [1, -1], "e": [1, 0]}
	for tiles in instr:
		pos = 0
		tile = [0, 0]
		while pos < len(tiles):
			dir = tiles[pos]
			if dir in "ns":
				pos += 1
				dir += tiles[pos]
			vec = dirs[dir]
			tile = [tile[0]+vec[0], tile[1]+vec[1]]
			pos += 1
		if tuple(tile) not in black:
			black.add(tuple(tile))
		else:
			black.remove(tuple(tile))
	return len(black)


def day24b():
	with open("2020/day24_input.txt", "r") as f:
		instr = f.read().strip().split('\n')
	black = set()
	dirs = {
		"ne": [0, 1], "nw": [-1, 1], "w": [-1, 0],
		"sw": [0, -1], "se": [1, -1], "e": [1, 0]}
	for tiles in instr:
		pos = 0
		tile = [0, 0]
		while pos < len(tiles):
			dir = tiles[pos]
			if dir in "ns":
				pos += 1
				dir += tiles[pos]
			vec = dirs[dir]
			tile = [tile[0]+vec[0], tile[1]+vec[1]]
			pos += 1
		if tuple(tile) not in black:
			black.add(tuple(tile))
		else:
			black.remove(tuple(tile))
	# At this point, black is initialized

	def get_boundary(blackset):
		boundary = set()
		for pos in blackset:
			for a, b in list(dirs.values()):
				boundary.add((pos[0]+a, pos[1]+b))
		boundary.update(blackset)
		return boundary
	
	boundary = get_boundary(black)

	def neighbours(pos):
		counter = 0
		for a, b in list(dirs.values()):
			if tuple([pos[0]+a, pos[1]+b]) in black:
				counter += 1
		return counter
	
	def cycle():
		nonlocal black, boundary
		newblack = set()
		for pos in boundary:
			n = neighbours(pos)
			if pos in black:
				if n == 1 or n == 2:
					newblack.add(pos)
			elif n == 2: # white
				newblack.add(pos)
		boundary = get_boundary(newblack)
		black = newblack
	
	for _ in range(100):
		cycle()
	
	return len(black)

print(day24b())
