from copy import deepcopy
from itertools import product


def day17a():
	with open("2020/day17_input.txt", "r") as f:
		instr = f.read().strip().split('\n')
	
	active = []

	# x=y=z=0 is top left of input
	for i in range(len(instr)):
		for j in range(len(instr[i])):
			if instr[i][j] == "#":
				active.append([i, j, 0])
	
	def neighbours(pos, activespace):
		count = 0
		for a in range(-1, 2):
			for b in range(-1, 2):
				for c in range(-1, 2):
					if a == b and b == c and c == 0:
						continue
					newpos = [pos[0] + a, pos[1] + b, pos[2] + c]
					if newpos in activespace:
						count += 1
		return count

	def newstate(pos, activespace):
		active = pos in activespace
		stay_active = [2, 3]
		if active:
			if neighbours(pos, activespace) in stay_active:
				return True
			return False
		else:
			if neighbours(pos, activespace) == 3:
				return True
			return False
	
	def cycle(activespace):
		xvals = [pos[0] for pos in activespace]
		yvals = [pos[1] for pos in activespace]
		zvals = [pos[2] for pos in activespace]
		newspace = []
		for x in range(min(xvals) - 1, max(xvals) + 2):
			for y in range(min(yvals) - 1, max(yvals) + 2):
				for z in range(min(zvals) - 1, max(zvals) + 2):
					posstate = newstate([x, y, z], activespace)
					if posstate:
						newspace.append([x, y, z])
		return newspace
	
	for _ in range(6):
		active = cycle(active)
	
	return len(active)

# Takes 5 minutes to run
def day17b():
	with open("2020/day17_input.txt", "r") as f:
		instr = f.read().strip().split('\n')
	
	active = []

	# x=y=z=w=0 is top left of input
	for i in range(len(instr)):
		for j in range(len(instr[i])):
			if instr[i][j] == "#":
				active.append([i, j, 0, 0])
	
	def neighbours(pos, activespace):
		count = 0
		for a in range(-1, 2):
			for b in range(-1, 2):
				for c in range(-1, 2):
					for d in range(-1, 2):
						if a == b and b == c and c == d and d == 0:
							continue
						newpos = [pos[0] + a, pos[1] + b, pos[2] + c, pos[3] + d]
						if newpos in activespace:
							count += 1
		return count

	def newstate(pos, activespace):
		active = pos in activespace
		stay_active = [2, 3]
		if active:
			if neighbours(pos, activespace) in stay_active:
				return True
			return False
		else:
			if neighbours(pos, activespace) == 3:
				return True
			return False
	
	def cycle(activespace):
		xvals = [pos[0] for pos in activespace]
		yvals = [pos[1] for pos in activespace]
		zvals = [pos[2] for pos in activespace]
		wvals = [pos[3] for pos in activespace]
		newspace = []
		for x in range(min(xvals) - 1, max(xvals) + 2):
			for y in range(min(yvals) - 1, max(yvals) + 2):
				for z in range(min(zvals) - 1, max(zvals) + 2):
					for w in range(min(wvals) - 1, max(wvals) + 2):
						posstate = newstate([x, y, z, w], activespace)
						if posstate:
							newspace.append([x, y, z, w])
		return newspace
	
	for _ in range(6):
		active = cycle(active)
	
	return len(active)

# Takes 2 minutes to run
def day17b2():
	with open("2020/day17_input.txt", "r") as f:
		instr = f.read().strip().split('\n')
	
	active = []
	boundary = set()

	# x=y=z=w=0 is top left of input
	for i in range(len(instr)):
		for j in range(len(instr[i])):
			if instr[i][j] == "#":
				active.append((i, j, 0, 0))
	
	def neighbours(pos, activespace):
		count = 0
		for a in range(-1, 2):
			for b in range(-1, 2):
				for c in range(-1, 2):
					for d in range(-1, 2):
						if a == b and b == c and c == d and d == 0:
							continue
						newpos = (pos[0] + a, pos[1] + b, pos[2] + c, pos[3] + d)
						if newpos in activespace:
							count += 1
		return count
	
	def get_neighbours(pos):
		neighbours = set()
		for a in range(-1, 2):
			for b in range(-1, 2):
				for c in range(-1, 2):
					for d in range(-1, 2):
						neighbours.add(
							(pos[0] + a, pos[1] + b, pos[2] + c, pos[3] + d))
		return neighbours

	def newstate(pos, activespace):
		if pos in activespace:
			return neighbours(pos, activespace) in [2, 3]
		else:
			return neighbours(pos, activespace) == 3
	
	def findboundary():
		xvals = [pos[0] for pos in active]
		yvals = [pos[1] for pos in active]
		zvals = [pos[2] for pos in active]
		wvals = [pos[3] for pos in active]
		boundary = set()
		for x in range(min(xvals) - 1, max(xvals) + 2):
			for y in range(min(yvals) - 1, max(yvals) + 2):
				for z in range(min(zvals) - 1, max(zvals) + 2):
					for w in range(min(wvals) - 1, max(wvals) + 2):
						if neighbours((x, y, z, w), active) > 0:
							boundary.add((x, y, z, w))
		return boundary
	
	def cycle(activespace, boundary):
		newspace = []
		newboundary = set()
		for p in boundary:
			if newstate(p, activespace):
				newspace.append(p)
				newboundary |= get_neighbours(p)
		return newspace, newboundary
	
	boundary = findboundary()
	for _ in range(6):
		active, boundary = cycle(active, boundary)
	
	return len(active)


def pos_add(p, q):
	return (p[0]+q[0], p[1]+q[1], p[2]+q[2], p[3]+q[3])

# Much faster!
def day17b3():
	with open("2020/day17_input.txt", "r") as f:
		instr = f.read().strip().split('\n')
	
	# Dict keys are (x, y, z, w)
	# Dict values are [active?, neighbours]
	active = {}

	# x=y=z=w=0 is top left of input
	for i in range(len(instr)):
		for j in range(len(instr[i])):
			if instr[i][j] == "#":
				pos = (i, j, 0, 0)
				# Add pos to active
				if pos not in active:
					active[pos] = [True, 0]
				else:
					active[pos][0] = True
				# Add all neighbours to active
				for vector in product(range(-1, 2), repeat=4):
					neighbour = pos_add(pos, vector)
					if neighbour == (i, j, 0, 0):
						continue
					if neighbour not in active:
						active[neighbour] = [False, 0]
					active[neighbour][1] += 1
	
	def neighbours(pos, activespace):
		count = 0
		for vector in product(range(-1, 2), repeat=4):
			neighbour = pos_add(pos, vector)
			if neighbour == pos:
				continue
			if neighbour in activespace and activespace[neighbour][0]:
				count += 1
		return count

	def newstate(pos, activespace):
		# Pos must be in activespace
		if activespace[pos][0]:
			return neighbours(pos, activespace) in [2, 3]
		else:
			return neighbours(pos, activespace) == 3
	
	def cycle(activespace):
		newspace = {}
		for p in activespace:
			if newstate(p, activespace):
				if p not in newspace:
					newspace[p] = [True, 0]
				else:
					newspace[p][0] = True
				# Add all neighbours to active
				for vector in product(range(-1, 2), repeat=4):
					neighbour = pos_add(p, vector)
					if neighbour == p:
						continue # FIX FROM HERE
					if neighbour not in newspace:
						newspace[neighbour] = [False, 0]
					newspace[neighbour][1] += 1
		return newspace
	
	for _ in range(6):
		active = cycle(active)
	
	return len([k for k in active.keys() if active[k][0]])


print(day17a())
print(day17b3())
