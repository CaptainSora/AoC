def day01a():
	with open("2015/day01_input.txt", "r") as f:
		brackets = f.read().strip()
	return brackets.count("(") - brackets.count(")")

def day01b():
	with open("2015/day01_input.txt", "r") as f:
		brackets = f.read().strip()
	floor = 0
	for i in range(len(brackets)):
		if brackets[i] == "(":
			floor += 1
		else:
			floor -= 1
		if floor == -1:
			return i + 1


print(day01a())
print(day01b())
