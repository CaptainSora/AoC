def day08a():
	with open("2022/day08_input.txt", "r") as f:
		trees = [
			[int(num) for num in row]
			for row in f.read().strip().split("\n")
		]
	nrows = len(trees)
	ncols = len(trees[0])
	trees_t = list(zip(*trees))
	visible = 2 * (nrows + ncols - 2)
	for r in range(1, nrows-1):
		for c in range(1, ncols-1):
			left = max(trees[r][:c])
			right = max(trees[r][c+1:])
			above = max(trees_t[c][:r])
			below = max(trees_t[c][r+1:])
			visible += trees[r][c] > min([left, right, above, below])
	return visible

def day08b():
	with open("2022/day08_input.txt", "r") as f:
		trees = [
			[int(num) for num in row]
			for row in f.read().strip().split("\n")
		]
	nrows = len(trees)
	ncols = len(trees[0])
	trees_t = list(zip(*trees))
	visible = 0
	
	def view(h, treeline):
		v = 0
		for idx in range(len(treeline)):
			v += 1
			if treeline[idx] >= h:
				break
		return v

	for r in range(1, nrows-1):
		for c in range(1, ncols-1):
			h = trees[r][c]
			left = view(h, trees[r][:c][::-1])
			right = view(h, trees[r][c+1:])
			above = view(h, trees_t[c][:r][::-1])
			below = view(h, trees_t[c][r+1:])
			visible = max(visible, left * right * above * below)
	return visible


print(day08a())
print(day08b())
