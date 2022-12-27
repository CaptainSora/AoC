from collections import deque


def day18a():
	with open("2022/day18_input.txt", "r") as f:
		cube = set([
			tuple([int(num) for num in line.split(",")])
			for line in f.read().strip().split("\n")
		])
	
	def surfacearea(c):
		nonlocal cube
		return sum([
			(c[0] + 1, c[1], c[2]) not in cube,
			(c[0] - 1, c[1], c[2]) not in cube,
			(c[0], c[1] + 1, c[2]) not in cube,
			(c[0], c[1] - 1, c[2]) not in cube,
			(c[0], c[1], c[2] + 1) not in cube,
			(c[0], c[1], c[2] - 1) not in cube
		])
	
	return sum([surfacearea(c) for c in cube])


def day18b():
	with open("2022/day18_input.txt", "r") as f:
		input = f.read().strip()
	cube = set([
		tuple([int(num) for num in line.split(",")])
		for line in input.split("\n")
	])
	nmax = max([
		int(num)
		for num in input.replace("\n", ",").split(",")
	])
	
	def neighbours(c):
		return [
			(c[0] + 1, c[1], c[2]),
			(c[0] - 1, c[1], c[2]),
			(c[0], c[1] + 1, c[2]),
			(c[0], c[1] - 1, c[2]),
			(c[0], c[1], c[2] + 1),
			(c[0], c[1], c[2] - 1)
		]
	
	outer = set()
	q = deque([(0, 0, 0)])
	while q:
		c = q.popleft()
		if -1 <= min(c) and max(c) <= nmax + 1:
			if c in outer or c in cube:
				continue
			else:
				outer.add(c)
				q.extend(neighbours(c))

	return sum([sum([n in outer for n in neighbours(c)]) for c in cube])
		

print(day18a())
print(day18b())
