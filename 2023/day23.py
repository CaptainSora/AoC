from itertools import count


def day23a():
	with open("2023/day23_input.txt", "r") as f:
		grid = f.read().strip().split("\n")
	
	def valid(r, c):
		return 0 <= r < len(grid) and 0 <= c < len(grid[0])
	
	def neighbours(r, c):
		"""
		Returns 4 neighbours as well as the slope they must be.
		"""
		return [(r+1, c, "v"), (r-1, c, "^"), (r, c+1, ">"), (r, c-1, "<")]

	def find_next_intersection(pos, nsteps=0, seen=set()):
		"""
		Returns (intersection_position, steps, next_steps).
		Assumes the first slope encountered precedes the intersection.
		"""
		slope = False
		r, c = pos
		seen.add(pos)
		for steps in count(nsteps + 1):
			for npos in neighbours(r, c):
				nr, nc, _ = npos
				if (nr, nc) in seen or not valid(nr, nc) or grid[nr][nc] == "#":
					continue
				# Update visted and step
				seen.add((nr, nc))
				r, c = nr, nc
				if slope:
					next_steps = [
						(r, c) for r, c, s in neighbours(nr, nc)
						if valid(r, c) and grid[r][c] == s
					]
					return (r, c), steps, next_steps
				elif grid[nr][nc] in "^>v<":
					slope = True
				break
			else:
				# Found no intersection, must be the end (or a dead end)
				return (r, c), steps - 1, []
	
	# Contract graph to vertices (intersections) and edge weights (steps)
	start = (0, 1)
	end = (len(grid) - 1, len(grid[0]) - 2)
	frontier = [(start, start, 0, set())]
	# Key: position as source intersection
	# Value: {position as destination intersection: steps}
	paths = {}
	paths[start] = {}
	while frontier:
		is_pos, *intersection = frontier.pop(0)
		id_pos, steps, next_steps = find_next_intersection(*intersection)
		# Check for second time at destination intersection
		if is_pos in paths and id_pos in paths[is_pos]:
			continue
		# Add to path list
		if is_pos not in paths:
			paths[is_pos] = {}
		paths[is_pos][id_pos] = steps
		# Add to frontier
		frontier.extend([(id_pos, pos, 1, set([id_pos])) for pos in next_steps])
	
	# Directed acyclic graph, already in topological order
	max_dist = {pos: 0 for pos in paths}
	max_dist[end] = 0
	for is_pos, routes in paths.items():
		for id_pos, steps in routes.items():
			max_dist[id_pos] = max(max_dist[id_pos], max_dist[is_pos] + steps)
	return max_dist[end]


def day23b():
	with open("2023/day23_input.txt", "r") as f:
		grid = f.read().strip().split("\n")
	
	def valid(r, c):
		return 0 <= r < len(grid) and 0 <= c < len(grid[0])
	
	def neighbours(r, c):
		"""
		Returns 4 neighbours as well as the slope they must be.
		"""
		return [(r+1, c, "v"), (r-1, c, "^"), (r, c+1, ">"), (r, c-1, "<")]

	def find_next_intersection(pos, nsteps=0, seen=set()):
		"""
		Returns (intersection_position, steps, next_steps).
		Assumes the first slope encountered precedes the intersection.
		"""
		slope = False
		r, c = pos
		seen.add(pos)
		for steps in count(nsteps + 1):
			for npos in neighbours(r, c):
				nr, nc, _ = npos
				if (nr, nc) in seen or not valid(nr, nc) or grid[nr][nc] == "#":
					continue
				# Update visted and step
				seen.add((nr, nc))
				r, c = nr, nc
				if slope:
					next_steps = [
						(r, c) for r, c, _ in neighbours(nr, nc)
						if valid(r, c) and grid[r][c] != "#"
						and (r, c) not in seen
					]
					return (r, c), steps, next_steps
				elif grid[nr][nc] in "^>v<":
					slope = True
				break
			else:
				# Found no intersection, must be the end (or a dead end)
				return (r, c), steps - 1, []
	
	# Contract graph to vertices (intersections) and edge weights (steps)
	start = (0, 1)
	end = (len(grid) - 1, len(grid[0]) - 2)
	frontier = [(start, start, 0, set())]
	# Key: position as source intersection
	# Value: {position as destination intersection: steps}
	paths = {}
	paths[start] = {}
	while frontier:
		is_pos, *intersection = frontier.pop(0)
		id_pos, steps, next_steps = find_next_intersection(*intersection)
		# Check for second time at destination intersection
		if is_pos in paths and id_pos in paths[is_pos]:
			continue
		# Add to path list
		if is_pos not in paths:
			paths[is_pos] = {}
		if id_pos not in paths:
			paths[id_pos] = {}
		paths[is_pos][id_pos] = steps
		paths[id_pos][is_pos] = steps
		# Add to frontier
		frontier.extend([(id_pos, pos, 1, set([id_pos])) for pos in next_steps])
	
	# Undirected cyclic graph, use fully exhaustive graph search
	visited = {pos: False for pos in paths}
	dist = {pos: 0 for pos in paths}
	
	def longest(pos, cur_steps):
		if visited[pos]:
			return
		visited[pos] = True
		dist[pos] = max(dist[pos], cur_steps)

		for dest, steps in paths[pos].items():
			longest(dest, cur_steps + steps)
		
		visited[pos] = False
	
	longest(start, 0)

	return dist[end]


print(day23a())
print(day23b())
