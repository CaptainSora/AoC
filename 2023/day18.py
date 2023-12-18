def day18a():
	with open("2023/day18_input.txt", "r") as f:
		plan = f.read().strip().split("\n")
	trench = set()
	pos = [0, 0]
	trench.add(tuple(pos))
	cw_edge = set()
	ccw_edge = set()
	# Dig edges
	dirs = {"R": [0, 1], "D": [1, 0], "L": [0, -1], "U": [-1, 0]}
	order = "RDLU"
	for row in plan:
		dir, dist, _ = row.split()
		# Track edges
		cw_idx, ccw_idx = (order.index(dir) + 1) % 4, (order.index(dir) - 1) % 4
		cw_pos = [pos[i] + dirs[order[cw_idx]][i] for i in range(2)]
		ccw_pos = [pos[i] + dirs[order[ccw_idx]][i] for i in range(2)]
		# Step and dig
		step = dirs[dir]
		for _ in range(int(dist)):
			pos = [pos[i] + step[i] for i in range(2)]
			trench.add(tuple(pos))
			cw_pos = [cw_pos[i] + step[i] for i in range(2)]
			cw_edge.add(tuple(cw_pos))
			ccw_pos = [ccw_pos[i] + step[i] for i in range(2)]
			ccw_edge.add(tuple(ccw_pos))
	cw_edge = cw_edge - trench
	ccw_edge = ccw_edge - trench
	adj = cw_edge if len(cw_edge) < len(ccw_edge) else ccw_edge
	# Find all interior
	inside = set()
	while adj:
		r, c = adj.pop()
		if (r, c) in inside or (r, c) in trench:
			continue
		inside.add((r, c))
		neighbours = [(r, c+1), (r+1, c), (r, c-1), (r-1, c)]
		for n in neighbours:
			if n not in trench and n not in adj and n not in inside:
				adj.add(n)
	return len(trench) + len(inside)


def day18b_old():
	"""
	Abandoned first draft. Folding sections outwards is edge case hell.
	"""
	with open("2023/day18_input.txt", "r") as f:
		plan = f.read().strip().split("\n")
	instr = []
	prev = int(plan[-1][-2])
	rot = 0
	for line in plan:
		dist = int(line[-7:-2], 16)
		dir = int(line[-2])
		instr.append([dir, dist])
		# Track rotation
		if (prev + 1) % 4 == dir:
			rot += 1
		else:
			rot -= 1
		prev = dir
	out = 1 if rot > 0 else -1
	print(out)
	area = 0
	while len(instr) > 4:
		# print(area, instr)
		for i in range(len(instr)):
			v, w, x, y, z = [instr[i+d][0] for d in range(-4, 1)]
			# Remove zeros
			if instr[i][1] == 0:
				del instr[i]
				break
			# Merge identical lines
			if y == z:
				instr[i][1] += instr[i-1][1]
				del instr[(i-1) % len(instr)]
				break
			# Fold corner outwards
			if w == y and x == z and (y + out) % 4 == z:
				# print(i, w, x, y, z)
				# Expand outwards
				instr[i-3][1] += instr[i-1][1]
				instr[i][1] += instr[i-2][1]
				area += instr[i-2][1] * instr[i-1][1]
				# Delete edges
				remove = [(i-2) % len(instr), (i-1) % len(instr)]
				for i in sorted(remove, reverse=True):
					del instr[i]
				break
			# Fold peninsula outwards
			# if v == x == z and (w + 2) % 4 == y and (y + out) % 4 == z:
			# 	# print(i, v, w, x, y, z)
			# 	# Select shorter and longer pair
			# 	par, adj, ladj, lpar = i, i-1, i-3, i-4
			# 	if instr[i-1][1] > instr[i-3][1]:
			# 		par, adj, ladj, lpar = lpar, ladj, adj, par
			# 	# Expand outwards
			# 	# print(instr[par][1], instr[adj][1], instr[-2][1], instr[ladj][1], instr[lpar][1])
			# 	instr[par][1] += instr[i-2][1]
			# 	instr[ladj][1] -= instr[adj][1]
			# 	area += instr[adj][1] * (instr[i-2][1] - 1)
			# 	remove = [adj % len(instr), (i-2) % len(instr)]
			# 	for i in sorted(remove, reverse=True):
			# 		del instr[i]
			# 	break
			if (w - out) % 4 == x and (x - out) % 4 == y and (y - out) % 4 != z:
				print("HERE")
				print(instr[i-4:i+2])
				# Find short edge
				short, long = i-3, i-1
				if instr[i-3][1] > instr[i-1][1]:
					short, long = long, short
				# Expand outwards
				instr[long][1] -= instr[short][1]
				area += instr[short][1] * (instr[i-2][1] - 1)
				del instr[short % len(instr)]
				if any([abs(instr[i][0] - instr[i-1][0]) == 2 for i in range(1, len(instr))]):
					print(instr[i-4:i+2])
					return "YIKES"
				break
		else:
			v, w, x, y, z = [instr[i+d][0] for d in range(-4, 1)]
			print(v == x == z, (w + 2) % 4 == y, (y + out) % 4 == z)
			print(instr[:7])
			print([tup[0] for tup in instr])
			return "OH NO"
	return (instr[0][1] + 1) * (instr[1][1] + 1) - area


def day18b():
	"""
	Second attempt, using the hints 'Shoelace Theorem' and 'Pick's Theorem'.
	"""
	with open("2023/day18_input.txt", "r") as f:
		plan = f.read().strip().split("\n")
	
	def cross(p1, p2):
		return p1[0] * p2[1] - p2[0] * p1[1]
	
	pos = [0, 0]
	area = 0
	perim = 0
	for line in plan:
		dist = int(line[-7:-2], 16)
		dir = int(line[-2])
		perim += dist
		step = [[0, 1], [1, 0], [0, -1], [-1, 0]][dir]
		new_pos = [pos[i] + step[i] * dist for i in range(2)]
		area += cross(pos, new_pos)
		pos = new_pos
	area = abs(area // 2)
	# Modified Pick's Theorem
	return area + perim // 2 + 1



print(day18a())
print(day18b())