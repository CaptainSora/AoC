from collections import deque


def day12a():
	with open("2022/day12_input.txt", "r") as f:
		hmap = f.read().strip().split("\n")
	h, w = len(hmap), len(hmap[0])
	S, E = [-1, -1], [-1, -1]
	# Find start and end points
	for i in range(len(hmap)):
		if S[1] == -1:
			S = [i, hmap[i].find("S")]
			hmap[i] = hmap[i].replace("S", "a")
		if E[1] == -1:
			E = [i, hmap[i].find("E")]
			hmap[i] = hmap[i].replace("E", "z")
	# Initialize BFS
	steps = [[-1 for _ in range(w)] for _ in range(h)]
	steps[S[0]][S[1]] = 0
	q = deque([S])
	while steps[E[0]][E[1]] < 0 and q:
		cell = q.popleft()
		neighbours = [
			[cell[0] + 1, cell[1]], [cell[0] - 1, cell[1]],
			[cell[0], cell[1] + 1], [cell[0], cell[1] - 1]
		]
		for n in neighbours:
			if n[0] < 0 or n[0] >= h or n[1] < 0 or n[1] >= w:
				continue
			if steps[n[0]][n[1]] > -1:
				continue
			if ord(hmap[n[0]][n[1]]) - ord(hmap[cell[0]][cell[1]]) < 2:
				steps[n[0]][n[1]] = steps[cell[0]][cell[1]] + 1
				q.append(n)
	return steps[E[0]][E[1]]


def day12b():
	with open("2022/day12_input.txt", "r") as f:
		hmap = f.read().strip().replace("S", "a").split("\n")
	h, w = len(hmap), len(hmap[0])
	E = [-1, -1]
	# Find start and end points
	for i in range(len(hmap)):
		if E[1] == -1:
			E = [i, hmap[i].find("E")]
			hmap[i] = hmap[i].replace("E", "z")
	# Initialize BFS
	steps = [[-1 for _ in range(w)] for _ in range(h)]
	steps[E[0]][E[1]] = 0
	q = deque([E])
	while q:
		cell = q.popleft()
		if hmap[cell[0]][cell[1]] == "a":
			return steps[cell[0]][cell[1]]
		neighbours = [
			[cell[0] + 1, cell[1]], [cell[0] - 1, cell[1]],
			[cell[0], cell[1] + 1], [cell[0], cell[1] - 1]
		]
		for n in neighbours:
			if n[0] < 0 or n[0] >= h or n[1] < 0 or n[1] >= w:
				continue
			if steps[n[0]][n[1]] > -1:
				continue
			if ord(hmap[cell[0]][cell[1]]) - ord(hmap[n[0]][n[1]]) < 2:
				steps[n[0]][n[1]] = steps[cell[0]][cell[1]] + 1
				q.append(n)


print(day12a())
print(day12b())
