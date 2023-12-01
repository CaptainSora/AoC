def day13a():
	with open("2021/day13_input.txt", "r") as f:
		dots, folds = f.read().strip().split("\n\n")
	dots = [[int(n) for n in line.split(",")] for line in dots.split("\n")]
	folds = [
		["xy".index(line[11]), int(line[13:])]
		for line in folds.split("\n")
	]
	dir, value = folds[0]
	for i in range(len(dots)):
		if dots[i][dir] > value:
			dots[i][dir] = 2 * value - dots[i][dir]
	return len(set([tuple(d) for d in dots]))
			


def day13b():
	with open("2021/day13_input.txt", "r") as f:
		dots, folds = f.read().strip().split("\n\n")
	dots = [[int(n) for n in line.split(",")] for line in dots.split("\n")]
	folds = [
		["xy".index(line[11]), int(line[13:])]
		for line in folds.split("\n")
	]
	bounds = [None, None]
	for fold in folds:
		dir, value = fold
		bounds[dir] = value
		for i in range(len(dots)):
			if dots[i][dir] > value:
				dots[i][dir] = 2 * value - dots[i][dir]
	dots = set([tuple(d) for d in dots])
	# Draw image
	for y in range(bounds[1]):
		print("".join([
			"#" if (x, y) in dots else "."
			for x in range(bounds[0])
		]))


print(day13a())
print(day13b())
