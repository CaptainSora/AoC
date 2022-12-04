from copy import deepcopy
from itertools import product
from math import prod


def day20a():
	with open("2020/day20_input.txt", "r") as f:
		tiles = [
			[
				t.split(":")[0][5:],
				[[char for char in row] for row in t.split("\n")[1:]]
			]
			for t in f.read().strip().split('\n\n')]

	
	def rotate(grid):
		return [list(row) for row in zip(*grid[::-1])]
	
	def rotateleft(grid):
		return rotate(rotate(rotate(grid)))
	
	def permute(grid):
		gridcopy = deepcopy(grid)
		retval = []
		for i in range(4):
			retval.append(gridcopy)
			gridcopy = rotate(gridcopy)
		gridcopy = gridcopy[::-1]
		for i in range(4):
			retval.append(gridcopy)
			gridcopy = rotate(gridcopy)
		return retval
	
	def match(g1, g2):
		# returns the rotation index where the two top rows match
		g1rot = permute(g1)
		g2rot = permute(g2)
		for i, j in product(range(8), repeat=2):
			if g1rot[i][0] == g2rot[j][0]:
				return [i, j]
		return [-1, -1]
	
	def printgrid(grid):
		print('\n'.join([''.join(row) for row in grid]))
		print()
	
	matches = []
	for t1 in tiles:
		counter = 0
		for t2 in tiles:
			if t1 == t2:
				continue
			if match(t1[1], t2[1]) != [-1, -1]:
				counter += 1
		matches.append([t1[0], counter])
	
	return prod([int(tile[0]) for tile in matches if tile[1] == 2])


def day20b():
	with open("2020/day20_input.txt", "r") as f:
		tiles = [[int(t.split(":")[0][5:]), [[char for char in row]
			for row in t.split("\n")[1:]]]
			for t in f.read().strip().split('\n\n')]
	
	pwidth = 12
	twidth = 10 - 2
	
	def rotate(grid):
		return [list(row) for row in zip(*grid[::-1])]
	
	def permute(grid):
		gridcopy = deepcopy(grid)
		retval = []
		for i in range(4):
			retval.append(gridcopy)
			gridcopy = rotate(gridcopy)
		gridcopy = gridcopy[::-1]
		for i in range(4):
			retval.append(gridcopy)
			gridcopy = rotate(gridcopy)
		return retval
	
	def match(g1, g2):
		# returns the rotation index where the two top rows are reversed
		g1rot = permute(g1)
		g2rot = permute(g2)
		for i, j in product(range(8), repeat=2):
			if g1rot[i][0] == g2rot[j][0][::-1]:
				return [i, j]
		return [-1, -1]
	
	def printgrid(grid):
		print('\n'.join([''.join(row) for row in grid]))
		print()
	
	def gettile(num):
		return [t[1] for t in tiles if t[0] == num][0]
	
	matches = {}
	for t1 in tiles:
		m = {}
		for t2 in tiles:
			if t1 == t2:
				continue
			matchval = match(t1[1], t2[1])
			if matchval != [-1, -1]:
				m[t2[0]] = matchval
		matches[t1[0]] = m
	
	photo = [[[] for _ in range(12)] for _ in range(12)]
	photoid = [[0 for _ in range(12)] for _ in range(12)]
	# corner and edges
	photoid[0][0] = [
		tile for tile in matches.keys() if len(matches[tile]) == 2
	][0]
	photo[0][0] = permute(gettile(photoid[0][0]))[7]
	# printgrid(photo[0][0])

	def strip(grid):
		return [row[1:-1] for row in grid[1:-1]]
	
	def match_right(g1, g2):
		# Assumes g1 is in correct orientation
		# returns g2 oriented correctly
		g2list = permute(g2)
		border = [row[-1] for row in g1] # right border top to bottom
		for g2r in g2list:
			if [row[0] for row in g2r] == border:
				return g2r
		return -1
	
	def match_below(g1, g2):
		# Assumes g1 is in correct orientation
		# returns g2 oriented correctly
		g2list = permute(g2)
		border = g1[-1] # bottom border left to right
		for g2r in g2list:
			if g2r[0] == border:
				return g2r
		return -1

	def already_placed(nid):
		return any([nid in row for row in photoid])

	def place():
		for r, c in product(range(pwidth), repeat=2):
			if r == 0 and c == 0:
				continue
			if c > 0: # match left
				prevgrid = photo[r][c-1]
				previd = photoid[r][c-1]
				neighbourids = list(matches[previd].keys())
				# remove unplaceable
				req = 4
				if r == 0 or r == pwidth-1:
					req -= 1
				if c == 0 or c == pwidth-1:
					req -= 1
				for nid in neighbourids:
					if len(matches[nid]) != req or already_placed(nid):
						continue
					testgrid = gettile(nid)
					matchgrid = match_right(prevgrid, testgrid)
					if matchgrid == -1:
						continue
					photo[r][c] = matchgrid
					photoid[r][c] = nid
					break
			else: # match above
				prevgrid = photo[r-1][c]
				previd = photoid[r-1][c]
				neighbourids = list(matches[previd].keys())
				# remove unplaceable
				req = 4
				if r == 0 or r == pwidth-1:
					req -= 1
				if c == 0 or c == pwidth-1:
					req -= 1
				for nid in neighbourids:
					if len(matches[nid]) != req or already_placed(nid):
						continue
					testgrid = gettile(nid)
					matchgrid = match_below(prevgrid, testgrid)
					if matchgrid == -1:
						continue
					photo[r][c] = matchgrid
					photoid[r][c] = nid
					break
			# printgrid(matchgrid)

	place()

	finalgrid = [['' for _ in range(pwidth*twidth)] for _ in range(pwidth*twidth)]
	for i, j in product(range(pwidth*twidth), repeat=2):
		i1 = int(i / twidth)
		j1 = int(j / twidth)
		i2 = i % twidth
		j2 = j % twidth
		finalgrid[i][j] = strip(photo[i1][j1])[i2][j2]
	
	printgrid(finalgrid)

	def findmonster(testgrid):
		mheight = 3
		mwidth = 20
		monster = [
			[0, 18], [1, 0],
			[1, 5], [1, 6], [1, 11], [1, 12], [1, 17], [1, 18], [1, 19],
			[2, 1], [2, 4], [2, 7], [2, 10], [2, 13], [2, 16],
		]
		count = 0
		for i in range(pwidth*twidth-mheight+1):
			for j in range(pwidth*twidth-mwidth+1):
				found = True
				for x, y in monster:
					if testgrid[i+x][j+y] != "#":
						found = False
						break
				if found:
					count += 1
					for x, y in monster:
						testgrid[i+x][j+y] = "O"
		if count > 0:
			return testgrid
		else:
			return 0
	
	for g in permute(finalgrid):
		testgrid = findmonster(g)
		if testgrid == 0:
			continue
		# printgrid(testgrid)
		return sum([row.count("#") for row in testgrid])
	return -1


print(day20a())
print(day20b())
