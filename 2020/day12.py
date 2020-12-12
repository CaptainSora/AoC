def day12a():
	with open("2020/day12_input.txt", "r") as f:
		instructions = f.read().strip().split('\n')
	
	dirs = ['E', 'S', 'W', 'N'] # left is -1, right is +1
	facing = 0
	vectors = [[1, 0], [0, -1], [-1, 0], [0, 1]]
	pos = [0, 0]

	def pos_mult(p, s):
		return [p[0] * s, p[1] * s]
	
	def pos_add(p, q):
		return [p[0] + q[0], p[1] + q[1]]

	for i in instructions:
		if i[0] in "LR":
			turn = int(int(i[1:])/90)
			dir = 1
			if i[0] == "L":
				dir = -1
			facing = (facing + dir * turn) % 4
		elif i[0] == "F":
			mag = int(i[1:])
			pos = pos_add(pos, pos_mult(vectors[facing], mag))
		else:
			mag = int(i[1:])
			pos = pos_add(pos, pos_mult(vectors[dirs.index(i[0])], mag))

	return abs(pos[0]) + abs(pos[1])

def day12b():
	with open("2020/day12_input.txt", "r") as f:
		instructions = f.read().strip().split('\n')
	
	dirs = ['E', 'S', 'W', 'N'] # left is -1, right is +1
	vectors = [[1, 0], [0, -1], [-1, 0], [0, 1]]
	waypoint = [10, 1]
	pos = [0, 0]

	def pos_mult(p, s):
		return [p[0] * s, p[1] * s]
	
	def pos_add(p, q):
		return [p[0] + q[0], p[1] + q[1]]
	
	def pos_rotate(p):
		return [p[1], -1 * p[0]]

	for i in instructions:
		if i[0] in "LR":
			turn = int(int(i[1:])/90) % 4
			if i[0] == "L":
				turn = 4 - turn
			for _ in range(turn):
				waypoint = pos_rotate(waypoint)
		elif i[0] == "F":
			mag = int(i[1:])
			pos = pos_add(pos, pos_mult(waypoint, mag))
		else:
			mag = int(i[1:])
			waypoint = pos_add(waypoint, pos_mult(vectors[dirs.index(i[0])], mag))

	return abs(pos[0]) + abs(pos[1])

print(day12b())
