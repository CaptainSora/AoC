from math import copysign


def day09a():
	with open("2022/day09_input.txt", "r") as f:
		instr = f.read().strip().split("\n")
	visited = set()
	head, tail = [0, 0], [0, 0]
	visited.add(tuple(tail))
	for line in instr:
		dir, mag = line.split()
		for _ in range(int(mag)):
			if dir == "U":
				head[1] += 1
			elif dir == "D":
				head[1] -= 1
			elif dir == "L":
				head[0] -= 1
			elif dir == "R":
				head[0] += 1
			diff = [head[0] - tail[0], head[1] - tail[1]]
			if max(abs(diff[0]), abs(diff[1])) == 2:
				if min(abs(diff[0]), abs(diff[1])) == 0:
					tail[0] += diff[0] // 2
					tail[1] += diff[1] // 2
				else:
					tail[0] += int(copysign(1, diff[0]))
					tail[1] += int(copysign(1, diff[1]))
			visited.add(tuple(tail))
	return len(visited)

def day09b():
	with open("2022/day09_input.txt", "r") as f:
		instr = f.read().strip().split("\n")
	visited = set()
	rope = [[0, 0] for _ in range(10)]
	visited.add(tuple(rope[-1]))
	for line in instr:
		dir, mag = line.split()
		for _ in range(int(mag)):
			if dir == "U":
				rope[0][1] += 1
			elif dir == "D":
				rope[0][1] -= 1
			elif dir == "L":
				rope[0][0] -= 1
			elif dir == "R":
				rope[0][0] += 1
			for i in range(1, len(rope)):
				diff = [rope[i-1][0] - rope[i][0], rope[i-1][1] - rope[i][1]]
				if max(abs(diff[0]), abs(diff[1])) == 2:
					if min(abs(diff[0]), abs(diff[1])) == 0:
						rope[i][0] += diff[0] // 2
						rope[i][1] += diff[1] // 2
					else:
						rope[i][1] += int(copysign(1, diff[1]))
						rope[i][0] += int(copysign(1, diff[0]))
			visited.add(tuple(rope[-1]))
	return len(visited)


print(day09a())
print(day09b())
