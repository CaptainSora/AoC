from itertools import product


class Brick:
	def __init__(self, num, ends):
		self.supports = set()
		self.supported_by = set()
		self.checked = False
		self.fallnum = 0
		self.num = num
		x, y, z = zip(*ends)
		self.pos = set()
		for i in range(min(x), max(x) + 1):
			for j in range(min(y), max(y) + 1):
				for k in range(min(z), max(z) + 1):
					self.pos.add((i, j, k))
	
	def fall(self):
		self.pos = set([(x, y, z-1) for x, y, z in self.pos])
	
	def minz(self):
		return min([z for x, y, z in self.pos])
	
	def above(self):
		return set([(x, y, z+1) for x, y, z in self.pos]) - self.pos


def day22a():
	with open("2023/day22_input.txt", "r") as f:
		bricks_snapshot = f.read().strip().split("\n")
	bricks_snapshot = [
		[tuple([int(num) for num in end.split(",")]) for end in line.split("~")]
		for line in bricks_snapshot
	]
	bricks_snapshot.sort(key=lambda x: min(x[0][-1], x[1][-1]))

	# Note that all x and y positions are 0-9 inclusive
	# This holds all the grid cubes which have support below them.
	support = set([(x, y, 1) for x, y in product(range(10), repeat=2)])
	origin = {}

	bricks = {num: Brick(num, pos) for num, pos in enumerate(bricks_snapshot)}

	def new_support(a, b):
		"""
		Creates the linked pair "a supports b".
		Uses brick numbers as access.
		"""
		nonlocal bricks
		bricks[a].supports.add(b)
		bricks[b].supported_by.add(a)
	
	falling_bricks = list(range(len(bricks_snapshot)))
	while falling_bricks:
		still_falling = []
		for i in falling_bricks:
			b = bricks[i]
			assert(i == b.num)
			below = support & b.pos
			if below:
				# Add linked pairs of supports
				for pos in below:
					if pos in origin:
						new_support(origin[pos], i)
				# Create new supports
				support |= b.above()
				for pos in b.above():
					origin[pos] = i
			else:
				# Mark as unstable
				still_falling.append(i)
		if len(still_falling) == len(falling_bricks):
			for i in still_falling:
				bricks[i].fall()
		falling_bricks = still_falling
	
	safe_disintegrate = []
	for num, b in bricks.items():
		assert(num == b.num)
		for s in b.supports:
			if len(bricks[s].supported_by) == 1:
				break
		else:
			safe_disintegrate.append(num)
	
	return len(safe_disintegrate)


def day22b():
	with open("2023/day22_input.txt", "r") as f:
		bricks_snapshot = f.read().strip().split("\n")
	bricks_snapshot = [
		[tuple([int(num) for num in end.split(",")]) for end in line.split("~")]
		for line in bricks_snapshot
	]
	bricks_snapshot.sort(key=lambda x: min(x[0][-1], x[1][-1]))

	# Note that all x and y positions are 0-9 inclusive
	# This holds all the grid cubes which have support below them.
	support = set([(x, y, 1) for x, y in product(range(10), repeat=2)])
	origin = {}

	bricks = {num: Brick(num, pos) for num, pos in enumerate(bricks_snapshot)}

	def new_support(a, b):
		"""
		Creates the linked pair "a supports b".
		Uses brick numbers as access.
		"""
		nonlocal bricks
		bricks[a].supports.add(b)
		bricks[b].supported_by.add(a)
	
	falling_bricks = list(range(len(bricks_snapshot)))
	while falling_bricks:
		still_falling = []
		for i in falling_bricks:
			b = bricks[i]
			assert(i == b.num)
			below = support & b.pos
			if below:
				# Add linked pairs of supports
				for pos in below:
					if pos in origin:
						new_support(origin[pos], i)
				# Create new supports
				support |= b.above()
				for pos in b.above():
					origin[pos] = i
			else:
				# Mark as unstable
				still_falling.append(i)
		if len(still_falling) == len(falling_bricks):
			for i in still_falling:
				bricks[i].fall()
		falling_bricks = still_falling
	
	# Calculate cascade for each brick
	for i in range(len(bricks_snapshot)):
		# Set self as falling. All bricks which rest only on falling bricks also
		#   become falling.
		falling = set([i])
		above = bricks[i].supports
		while above:
			next_above = set()
			for s in above:
				if not (bricks[s].supported_by - falling):
					falling.add(s)
					next_above |= bricks[s].supports
			above = next_above
		bricks[i].fallnum = len(falling) - 1

	return sum([b.fallnum for b in bricks.values()])


print(day22a())
print(day22b())
