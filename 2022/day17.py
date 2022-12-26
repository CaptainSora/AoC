def day17a():
	with open("2022/day17_input.txt", "r") as f:
		jet = f.read().strip()
	solid = set([(0, w) for w in range(7)])
	highest = 0
	rocks = [
		[[3, 2], [3, 3], [3, 4], [3, 5]], # Horizontal
		[[3, 3], [4, 2], [4, 3], [4, 4], [5, 3]], # Cross
		[[3, 2], [3, 3], [3, 4], [4, 4], [5, 4]], # L
		[[3, 2], [4, 2], [5, 2], [6, 2]], # Vertical
		[[3, 2], [3, 3], [4, 2], [4, 3]] # Square
	]

	def move(rock, h=0, w=0):
		return [[r[0] + h, r[1] + w] for r in rock]
	
	def jetgen():
		nonlocal jet
		while True:
			for c in jet:
				if c == ">":
					yield 1
				elif c == "<":
					yield -1
	
	def valid(rock):
		return all([0 <= w < 7 for w in list(zip(*rock))[1]])
	
	def stopped(rock):
		nonlocal solid
		return any([tuple(r) in solid for r in rock])
		
	jg = jetgen()
	for i in range(2022):
		rock = move(rocks[i%5], h=highest+1)
		while True:
			# Jet sideways
			nrock = move(rock, w=next(jg))
			if valid(nrock) and not stopped(nrock):
				rock = nrock
			# Fall down
			nrock = move(rock, h=-1)
			if stopped(nrock):
				solid.update([tuple(r) for r in rock])
				highest = max(highest, max(list(zip(*rock))[0]))
				break
			rock = nrock
	return highest
		



def day17b():
	with open("2022/day17_input.txt", "r") as f:
		jet = f.read().strip()
	solid = set([(0, w) for w in range(7)])
	highest = 0
	rocks = [
		[(3, 2), (3, 3), (3, 4), (3, 5)], # Horizontal
		[(3, 3), (4, 2), (4, 3), (4, 4), (5, 3)], # Cross
		[(3, 2), (3, 3), (3, 4), (4, 4), (5, 4)], # L
		[(3, 2), (4, 2), (5, 2), (6, 2)], # Vertical
		[(3, 2), (3, 3), (4, 2), (4, 3)] # Square
	]

	def move(rock, h=0, w=0):
		return [[r[0] + h, r[1] + w] for r in rock]
	
	def jetgen():
		nonlocal jet
		while True:
			for c in jet:
				if c == ">":
					yield 1
				elif c == "<":
					yield -1
	
	def valid(rock):
		return all([0 <= w < 7 for w in list(zip(*rock))[1]])
	
	def stopped(rock):
		nonlocal solid
		return any([tuple(r) in solid for r in rock])
		
	jg = jetgen()
	for i in range(1000000000000):
		rock = move(rocks[i%5], h=highest+1)
		while True:
			# Jet sideways
			nrock = move(rock, w=next(jg))
			if valid(nrock) and not stopped(nrock):
				rock = nrock
			# Fall down
			nrock = move(rock, h=-1)
			if stopped(nrock):
				solid.update([tuple(r) for r in rock])
				highest = max(highest, max(list(zip(*rock))[0]))
				break
			rock = nrock
	return highest


print(day17a())
print(day17b())
