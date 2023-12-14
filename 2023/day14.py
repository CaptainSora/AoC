# https://adventofcode.com/2023/leaderboard/day/14


def day14a():
	with open("2023/day14_input.txt", "r") as f:
		dish = f.read().strip().split("\n")
	nrows = len(dish)
	total_weight = 0
	# Transpose, shift left instead of up
	dish = ["".join(col) for col in zip(*dish)]
	for row in dish:
		stop = -1
		for pos, rock in enumerate(row):
			if rock == "#":
				stop = pos
			elif rock == "O":
				stop += 1
				total_weight += nrows - stop
	return total_weight


def day14b():
	with open("2023/day14_input.txt", "r") as f:
		dish = f.read().strip().split("\n")
	nrows = len(dish)
	# Transpose, North is left
	dish = ["".join(col) for col in zip(*dish)]

	def cycle(dish):
		"""
		Runs a "spin cycle" on the rocks.
		Assumes the input is transposed so that North is left and West is up.
		"""
		for rev in [True, True, False, False]:
			# Roll and tranpose
			dish = ["".join(col) for col in zip(*[
				"#".join(["".join(sorted(part, reverse=rev)) for part in row.split("#")])
				for row in dish
			])]
		return dish
	
	dish_hist = {}
	ncycles = 0
	# Run cycles until returning to an existing pattern
	while True:
		dish = cycle(dish)
		ncycles += 1
		key = "\n".join(dish)
		if key in dish_hist:
			break
		dish_hist[key] = ncycles
	# Compute period length and step to the end
	diff = ncycles - dish_hist[key]
	for _ in range((1000000000 - ncycles) % diff):
		dish = cycle(dish)
	# Return weight
	return sum([
		nrows - pos
		for row in dish
		for pos, rock in enumerate(row)
		if rock == "O"
	])


print(day14a())
print(day14b())
