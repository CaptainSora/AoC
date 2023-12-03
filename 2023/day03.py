def day03a():
	with open("2023/day03_input.txt", "r") as f:
		engine = f.read().strip().split("\n")
	part_sum = 0
	# Find all numbers and search their bounding boxes
	for lnum, line in enumerate(engine):
		line_copy = "".join([c if c.isdecimal() else "." for c in line])
		nums = [n for n in line_copy.split(".") if n]
		# Stupid oversight: gotta tell find() where to start looking!
		left = 0
		for num in nums:
			idx = line.find(num, left)
			i = max(0, idx - 1)
			j = min(idx + len(num) + 1, len(line))
			search = ""
			if lnum > 0:
				search += engine[lnum - 1][i:j]
			search += engine[lnum][i:j]
			if lnum + 1 < len(engine):
				search += engine[lnum + 1][i:j]
			search = search.replace(".", "")
			if not search.isdecimal():
				# There are non-decimal, non-period values left
				part_sum += int(num)
			# Ignore everything before this
			left = j - 1
	return part_sum


def day03b():
	with open("2023/day03_input.txt", "r") as f:
		engine = f.read().strip().split("\n")
	gears = {}

	def gear_adj(line, idx, numstr):
		nonlocal gears
		if (line, idx) not in gears:
			gears[(line, idx)] = []
		gears[(line, idx)].append(int(numstr))

	# Find all numbers and search their bounding boxes
	for lnum, line in enumerate(engine):
		line_copy = "".join([c if c.isdecimal() else "." for c in line])
		nums = [n for n in line_copy.split(".") if n]
		left = 0
		for num in nums:
			idx = line.find(num, left)
			i = max(0, idx - 1)
			j = min(idx + len(num) + 1, len(line))
			# Search above
			if lnum > 0:
				pos = engine[lnum - 1][i:j].find("*")
				if pos > -1:
					gear_adj(lnum - 1, i + pos, num)
			# Search left and right
			if line[i] == "*":
				gear_adj(lnum, i, num)
			if line[j-1] == "*":
				gear_adj(lnum, j-1, num)
			# Search below
			if lnum + 1 < len(engine):
				pos = engine[lnum + 1][i:j].find("*")
				if pos > -1:
					gear_adj(lnum + 1, i + pos, num)
			# Ignore everything before this
			left = j - 1
	
	return sum([v[0] * v[1] for k, v in gears.items() if len(v) == 2])


print(day03a())
print(day03b())
