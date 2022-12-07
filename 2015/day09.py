from itertools import combinations


class TSP:
	def __init__(self, dist, dtype=int, cycle=True):
		"""
		Distances must be given as [city1, city2, dist]
		dist must be castable as dtype, which must be a numeric type
		cycle=True finds the shortest Hamiltonian cycle
		cycle=False finds the shortest Hamiltonian path
		  not necessarily contained in the cycle, but reducible
		"""
		self.nodes = list(set([
			city for order in list(zip(*dist))[:2] for city in order]))
		self.cycle = cycle
		if not self.cycle:
			self.nodes.append("Universal Node")
		self.dist = [
			[0 for _ in range(len(self.nodes))]
			for _ in range(len(self.nodes))
		]
		for line in dist:
			city1, city2, d = line
			city1, city2 = self.nodes.index(city1), self.nodes.index(city2)
			self.dist[city1][city2] = dtype(d)
			self.dist[city2][city1] = dtype(d)
		# Stores partial solutions
		self.g = {} # Distances
		self.p = {} # Previous nodes
		# Stores the optimal solution
		self.opt = None
		self.path = None
	
	def solve(self, choice=min):
		"""
		Uses the Held-Karp algorithm to find an exact solution to the TSP.
		Time complexity: O(2^n * n^2)
		Space complexity: O(n * 2^n)
		choice: aggregate function for which option to choose
		"""
		others = list(range(1, len(self.nodes)))

		# Initialize first distances
		for k in range(1, len(self.nodes)):
			self.g[((k,), k)] = self.dist[0][k]
			self.p[((k,), k)] = 0
		
		# Iteratively add longer distances
		for s in range(2, len(self.nodes)):
			for comb in combinations(others, r=s):
				for k in comb:
					remain = list(comb)
					remain.remove(k)
					options = [
						self.g[(tuple(remain), m)] + self.dist[m][k]
						for m in remain
					]
					self.g[(comb, k)] = choice(options)
					self.p[(comb, k)] = remain[options.index(choice(options))]
		
		# Find final distance
		options = [
			self.g[(tuple(others), k)] + self.dist[k][0]
			for k in range(1, len(self.nodes))
		]
		self.opt = choice(options)
		# Find path
		self.path = [0, 1 + options.index(self.opt)]
		while self.path[-1] != 0:
			self.path.append(self.p[(tuple(others), self.path[-1])])
			others.remove(self.path[-2])
	
	def prettyprint(self):
		if not self.cycle:
			idx = self.path.index(len(self.nodes)-1)
			self.path = self.path[idx+1:-1] + self.path[:idx]
		dist = [
			self.dist[self.path[i-1]][self.path[i]]
			for i in range(1, len(self.path))
		]
		assert(sum(dist) == self.opt)
		# Print path
		path = [self.nodes[p] for p in self.path]
		print(" -> ".join(path))
		for i in range(len(path) - 1):
			print(
				f"{path[i]} -> {path[i+1]}"
				f" ({dist[i]})"
			)


def day09a():
	with open("2015/day09_input.txt", "r") as f:
		dists = [
			line.split(" = ") 
			for line in f.read().replace("to", "=").strip().split("\n")
		]
	tsp = TSP(dists, cycle=False)
	tsp.solve()
	# tsp.prettyprint()
	return tsp.opt
	

def day09b():
	with open("2015/day09_input.txt", "r") as f:
		dists = [
			line.split(" = ") 
			for line in f.read().replace("to", "=").strip().split("\n")
		]
	tsp = TSP(dists, cycle=False)
	tsp.solve(choice=max)
	# tsp.prettyprint()
	return tsp.opt


print(day09a())
print(day09b())
