def day02a():
	with open("2021/day02_input.txt", "r") as f:
		inputs = f.read().strip().split("\n")
	depth = 0
	position = 0
	for input in inputs:
		dir, mag = input.split()
		if dir == "forward":
			position += int(mag)
		elif dir == "down":
			depth += int(mag)
		elif dir == "up":
			depth -= int(mag)
	return depth * position

def day02b():
	with open("2021/day02_input.txt", "r") as f:
		inputs = f.read().strip().split("\n")
	depth = 0
	position = 0
	aim = 0
	for input in inputs:
		dir, mag = input.split()
		if dir == "forward":
			position += int(mag)
			depth += aim * int(mag)
		elif dir == "down":
			aim += int(mag)
		elif dir == "up":
			aim -= int(mag)
	return depth * position


print(day02a())
print(day02b())
