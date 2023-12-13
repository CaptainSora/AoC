def day13a():
	with open("2023/day13_input.txt", "r") as f:
		valleys = f.read().strip().split("\n\n")
	notes = 0

	def find_mirror(valley):
		"""
		Looks for a horizontal mirror in the valley.
		Returns the number of rows above the mirror, or 0 if none.
		"""
		nrows = len(valley)
		possible_rows = []
		for idx, row in enumerate(valley[:-1]):
			if row == valley[idx+1]:
				possible_rows.append(idx+1)
		for row in possible_rows:
			max_rows = min(nrows - row, row)
			for i in range(max_rows):
				left, right = row - i - 1, row + i
				if valley[left] != valley[right]:
					break
			else: # nobreak, valid
				return row
		return 0

	for valley in valleys:
		valley = valley.strip().split("\n")
		# Check horizontal mirror
		v_note = find_mirror(valley)
		if v_note:
			notes += 100 * v_note
			continue
		# Check vertical mirror:
		valley_t = ["".join(col) for col in zip(*valley)]
		v_note = find_mirror(valley_t)
		if v_note:
			notes += v_note
	
	return notes


def day13b():
	with open("2023/day13_input.txt", "r") as f:
		valleys = f.read().strip().split("\n\n")
	notes = 0

	def find_mirror(valley):
		"""
		Looks for a horizontal mirror with one smudge in the valley.
		Returns the number of rows above the mirror, or 0 if none.
		"""
		nrows = len(valley)
		for row in range(1, len(valley)):
			max_rows = min(nrows - row, row)
			errors = 0
			for i in range(max_rows):
				left, right = row - i - 1, row + i
				# Match string
				if valley[left] != valley[right]:
					errors += sum([
						1 for a, b in zip(valley[left], valley[right]) 
						if a != b
					])
				if errors > 1:
					break
			if errors == 1:
				return row
		return 0
	
	for valley in valleys:
		valley = valley.strip().split("\n")
		# Check horizontal mirror
		v_note = find_mirror(valley)
		if v_note:
			notes += 100 * v_note
			continue
		# Check vertical mirror:
		valley_t = ["".join(col) for col in zip(*valley)]
		v_note = find_mirror(valley_t)
		if v_note:
			notes += v_note
	
	return notes


print(day13a())
print(day13b())
