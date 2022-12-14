from collections import deque
from math import prod


def day09a():
	with open("2021/day09_input.txt", "r") as f:
		hmap = [
			[int(num) for num in row]
			for row in f.read().strip().split("\n")
		]
	nrows, ncols = len(hmap), len(hmap[0])
	risksum = 0
	for r in range(nrows):
		for c in range(ncols):
			neighbours = [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]
			for n in neighbours:
				if n[0] < 0 or n[0] >= nrows or n[1] < 0 or n[1] >= ncols:
					continue
				if hmap[n[0]][n[1]] <= hmap[r][c]:
					break
			else:
				risksum += hmap[r][c] + 1
	return risksum
	

def day09b():
	with open("2021/day09_input.txt", "r") as f:
		hmap = [
			[int(num) for num in row]
			for row in f.read().strip().split("\n")
		]
	nrows, ncols = len(hmap), len(hmap[0])
	lowpts = []
	basindict = {}
	for r in range(nrows):
		for c in range(ncols):
			if hmap[r][c] == 9:
				continue
			neighbours = [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]
			for n in neighbours:
				if n[0] < 0 or n[0] >= nrows or n[1] < 0 or n[1] >= ncols:
					continue
				if hmap[n[0]][n[1]] < hmap[r][c]:
					tn = tuple(n)
					if tn not in basindict:
						basindict[tn] = []
					basindict[tn].append((r, c))
					break
			else:
				lowpts.append((r, c))
	basinsizes = []
	for l in lowpts:
		basin = deque(basindict[l])
		bsize = 1
		while basin:
			next = basin.popleft()
			bsize += 1
			basin.extend(basindict.get(next, []))
		basinsizes.append(bsize)
	basinsizes.sort(reverse=True)
	return prod(basinsizes[:3])


print(day09a())
print(day09b())
