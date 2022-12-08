class GoL:
	"""
	Implements Conway's Game of Life.
	"""
	def __init__(self, grid, alive="#", dead=".", remain=[2, 3], new=[3]):
		"""
		grid is stored as a list of strings, where each string denotes a row
		(alive, dead) represents the icon used to denote a cell's status
		remain denotes how many neighbours a cell must have to remain alive
		new denotes how many neighbours a cell must have to become alive
		"""
		self.grid = grid
		self.xmax = len(self.grid) - 1
		self.ymax = len(self.grid[0]) - 1
		self.alive = alive
		self.dead = dead
		self.remain = remain
		self.new = new
	
	def neighbors(self, x, y):
		"""
		Returns the number of alive neighbours.
		"""
		coords = [(x+i, y+j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
		n = 0
		for c in coords:
			if c[0] == x and c[1] == y:
				continue
			elif c[0] < 0 or c[1] < 0:
				continue
			elif c[0] > self.xmax or c[1] > self.ymax:
				continue
			n += self.grid[c[0]][c[1]] == self.alive
		return n
	
	def newstate(self, x, y):
		n = self.neighbors(x, y)
		if self.grid[x][y] == self.alive and n in self.remain:
			return self.alive
		elif self.grid[x][y] == self.dead and n in self.new:
			return self.alive
		return self.dead
	
	def step(self):
		newgrid = []
		for x in range(self.xmax+1):
			row = ""
			for y in range(self.ymax+1):
				row += self.newstate(x, y)
			newgrid.append(row)
		self.grid = newgrid
	
	def count(self):
		return sum([row.count(self.alive) for row in self.grid])



def day18a():
	with open("2015/day18_input.txt", "r") as f:
		grid = f.read().strip().split("\n")
	gol = GoL(grid)
	for _ in range(100):
		gol.step()
	return gol.count()

def day18b():
	with open("2015/day18_input.txt", "r") as f:
		grid = f.read().strip().split("\n")
	gol = GoL(grid)
	gol.grid[0] = gol.alive + gol.grid[0][1:-1] + gol.alive
	gol.grid[-1] = gol.alive + gol.grid[-1][1:-1] + gol.alive
	for _ in range(100):
		gol.step()
		gol.grid[0] = gol.alive + gol.grid[0][1:-1] + gol.alive
		gol.grid[-1] = gol.alive + gol.grid[-1][1:-1] + gol.alive
	return gol.count()


print(day18a())
print(day18b())
