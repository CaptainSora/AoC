def day14a():
	with open("2022/day14_input.txt", "r") as f:
		rock = f.read().strip().split("\n")
	solid = set()
	max_d = 0
	# Set all the rocks
	for line in rock:
		line = [
			[int(num) for num in pair.split(",")]
			for pair in line.split(" -> ")
		]
		for i in range(1, len(line)):
			x1, y1, x2, y2 = *line[i-1], *line[i]
			max_d = max(max_d, y1, y2)
			solid.update([
				(x, y)
				for x in range(min(x1, x2), max(x1, x2) + 1)
				for y in range(min(y1, y2), max(y1, y2) + 1)
			])
	nrock = len(solid)
	# Start simulating sand
	solid_sand = 0
	while True:
		sandx, sandy = 500, 0
		while True:
			if (sandx, sandy + 1) not in solid:
				sandy += 1
				if sandy > max_d:
					return len(solid) - nrock
			elif (sandx - 1, sandy + 1) not in solid:
				sandx -= 1
				sandy += 1
			elif (sandx + 1, sandy + 1) not in solid:
				sandx += 1
				sandy += 1
			else:
				solid.add((sandx, sandy))
				solid_sand += 1
				break


def day14b():
	with open("2022/day14_input.txt", "r") as f:
		rock = f.read().strip().split("\n")
	solid = set()
	max_d = 0
	# Set all the rocks
	for line in rock:
		line = [
			[int(num) for num in pair.split(",")]
			for pair in line.split(" -> ")
		]
		for i in range(1, len(line)):
			x1, y1, x2, y2 = *line[i-1], *line[i]
			max_d = max(max_d, y1, y2)
			solid.update([
				(x, y)
				for x in range(min(x1, x2), max(x1, x2) + 1)
				for y in range(min(y1, y2), max(y1, y2) + 1)
			])
	nrock = len(solid)
	cave_floor = max_d + 2
	# Start simulating sand
	solid_sand = 0
	while (500, 0) not in solid:
		sandx, sandy = 500, 0
		while True:
			if sandy + 1 == cave_floor:
				solid.add((sandx, sandy))
				solid_sand += 1
				break
			elif (sandx, sandy + 1) not in solid:
				sandy += 1
			elif (sandx - 1, sandy + 1) not in solid:
				sandx -= 1
				sandy += 1
			elif (sandx + 1, sandy + 1) not in solid:
				sandx += 1
				sandy += 1
			else:
				solid.add((sandx, sandy))
				solid_sand += 1
				break
	return len(solid) - nrock


print(day14a())
print(day14b())
