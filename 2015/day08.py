def day08a():
	with open("2015/day08_input.txt", "r") as f:
		santa = f.read().strip().split("\n")
	chrdiff = 0
	for line in santa:
		chrdiff += len(line)
		escape = 0
		for chr in line[1:-1]:
			if escape and chr == "x":
				escape = 2
			elif escape:
				escape -= 1
				if not escape:
					chrdiff -= 1
			elif chr == "\\":
				escape = 1
			else:
				chrdiff -= 1
	return chrdiff

def day08b():
	with open("2015/day08_input.txt", "r") as f:
		santa = f.read().strip().split("\n")
	return sum([2 + line.count("\\") + line.count('"') for line in santa])


print(day08a())
print(day08b())
