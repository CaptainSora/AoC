def day16a():
	with open("2023/day16_input.txt", "r") as f:
		grid = f.read().strip().split("\n")
	# Using (r, c) order
	beams = [([0, 0], [0, 1])]
	energized = set()
	while beams:
		pos, dir = beams.pop(0)
		key = (tuple(pos), tuple(dir))
		if pos[0] < 0 or pos[0] >= len(grid):
			continue
		if pos[1] < 0 or pos[1] >= len(grid):
			continue
		if key in energized:
			continue
		energized.add(key)
		dir_split = None
		tile = grid[pos[0]][pos[1]]
		if tile == "\\":
			dir = dir[::-1]
		elif tile == "/":
			dir = [-1 * num for num in dir[::-1]]
		elif tile == "-" and dir[0] != 0:
			dir, dir_split = [0, 1], [0, -1]
		elif tile == "|" and dir[1] != 0:
			dir, dir_split = [1, 0], [-1, 0]
		new_pos = [pos[i] + dir[i] for i in range(2)]
		beams.append((new_pos, dir))
		if dir_split is not None:
			new_pos_split = [pos[i] + dir_split[i] for i in range(2)]
			beams.append((new_pos_split, dir_split))
	tiles = set([pair[0] for pair in energized])
	return len(tiles)


def day16b():
	with open("2023/day16_input.txt", "r") as f:
		grid = f.read().strip().split("\n")
	max_energized = []
	# Using (r, c) order
	edges = [
		[([x, 0], [0, 1])] for x in range(len(grid))
	] + [
		[([x, len(grid[0]) - 1], [0, -1])] for x in range(len(grid))
	] + [
		[([0, y], [1, 0])] for y in range(len(grid[0]))
	] + [
		[([len(grid) - 1, y], [-1, 0])] for y in range(len(grid[0]))
	]
	for beams in edges:
		energized = set()
		while beams:
			pos, dir = beams.pop(0)
			key = (tuple(pos), tuple(dir))
			if pos[0] < 0 or pos[0] >= len(grid):
				continue
			if pos[1] < 0 or pos[1] >= len(grid):
				continue
			if key in energized:
				continue
			energized.add(key)
			dir_split = None
			tile = grid[pos[0]][pos[1]]
			if tile == "\\":
				dir = dir[::-1]
			elif tile == "/":
				dir = [-1 * num for num in dir[::-1]]
			elif tile == "-" and dir[0] != 0:
				dir, dir_split = [0, 1], [0, -1]
			elif tile == "|" and dir[1] != 0:
				dir, dir_split = [1, 0], [-1, 0]
			new_pos = [pos[i] + dir[i] for i in range(2)]
			beams.append((new_pos, dir))
			if dir_split is not None:
				new_pos_split = [pos[i] + dir_split[i] for i in range(2)]
				beams.append((new_pos_split, dir_split))
		max_energized.append(len(set([pair[0] for pair in energized])))
	return max(max_energized)


print(day16a())
print(day16b())
