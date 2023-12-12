from itertools import zip_longest


def partition(n, b):
	"""
	Returns every partition of n identical objects into b buckets.
	"""
	parts = []
	# No objects
	if n == 0:
		return [[0 for _ in range(b)]]
	# One bucket
	if b == 1:
		return [[n]]
	# Else
	for i in range(n+1):
		for sub in partition(n-i, b-1):
			parts.append([i] + sub)
	return parts


def match(record, sample):
	"""
	Returns True if sample is a possible match for record.
	Requires record and sample to be the same length.
	"""
	for i, char in enumerate(record):
		if char != "?" and record[i] != sample[i]:
			return False
	return True


LOOKUP = {}

def search(arr, grp):
	"""
	Performs a recursive search of the arrangement given a grouping.
	"""
	global LOOKUP
	# Memoization
	key = arr + ",".join([str(num) for num in grp])
	if key in LOOKUP:
		return LOOKUP[key]
	# Counter
	count = 0
	# Base case
	if len(grp) == 1:
		fillers = len(arr) - grp[0]
		for i in range(fillers + 1):
			j = fillers - i
			sample = "." * i + "#" * grp[0] + "." * j
			count += int(match(arr, sample))
	# Recursive case
	else:
		sample = "#" * grp[0] + "."
		first_hash = arr.find("#") if "#" in arr else len(arr)
		lim = min(first_hash, len(arr) - (sum(grp) + len(grp) - 1))
		for i in range(lim + 1):
			if match(arr[i:i+grp[0]+1], sample):
				count += search(arr[i+grp[0]+1:], grp[1:])
	LOOKUP[key] = count
	return count


# First attempt preserved for history
def day12a():
	with open("2023/day12_input.txt", "r") as f:
		records = f.read().strip().split("\n")
	match_counts = 0
	
	for line in records:
		arr, grp = line.split()
		grp = [int(num) for num in grp.split(",")]
		dmg = ["#" * num for num in grp]
		spacing = [0] + [1 for _ in range(len(grp) - 1)] + [0]
		leftover = len(arr) - sum(grp) - sum(spacing)
		for part in partition(leftover, len(spacing)):
			opr = ["." * (part[i] + spacing[i]) for i in range(len(spacing))]
			sample = "".join([
				num
				for tup in zip_longest(opr, dmg)
				for num in tup
				if num is not None
			])
			if match(arr, sample):
				match_counts += 1	
	return match_counts


def day12b():
	with open("2023/day12_input.txt", "r") as f:
		records = f.read().strip().split("\n")
	match_counts = 0
	mult = 5
	
	for line in records:
		arr, grp = line.split()
		grp = [int(num) for num in grp.split(",")]
		# Part B modification
		f_arr = "?".join([arr] * mult)
		f_grp = [grp[i % len(grp)] for i in range(len(grp) * mult)]
		match_counts += search(f_arr, f_grp)
	return match_counts
	

print(day12a())
print(day12b())