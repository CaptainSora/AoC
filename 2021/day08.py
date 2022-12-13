def day08a():
	with open("2021/day08_input.txt", "r") as f:
		signals = f.read().replace("| ", "").strip().split("\n")
	return len([
		len(seg)
		for line in signals
		for seg in line.split()[10:]
		if len(seg) in [2, 3, 4, 7]
	])


def day08b():
	with open("2021/day08_input.txt", "r") as f:
		signals = f.read().replace("| ", "").strip().split("\n")
	# length 2: 1 (can identify c/f)
	# length 3: 7
	# length 4: 4 (can identify b/d)
	# length 5: 2, 3, 5 (differ on b/c and e/f)
	# length 6: 0, 6, 9 (differ on c/d/e)
	# length 7: 8
	# if L6 and shares all(4) with L4(4): 9
	# elif L6 and shares all(2) with L2(1): 0
	# else, L6 is 6
	# if L5 and shares all with 6: 5
	# elif L5 and shares 3 with L4(4): 3
	# else, L5 is 2
	total = 0
	for line in signals:
		line = [frozenset(d) for d in line.split()]
		check, output = line[:10], line[10:]
		check.sort(key=lambda x: len(x))
		# Identify all 10 digits
		digits = {check[0]: 1, check[1]: 7, check[2]: 4, check[9]: 8}
		six = frozenset()
		for d in check[8:2:-1]:
			if len(d) == 6:
				if len(d & check[2]) == 4:
					digits[d] = 9
				elif len(d & check[0]) == 2:
					digits[d] = 0
				else:
					digits[d] = 6
					six = d
			elif len(d) == 5:
				if len(d & six) == 5:
					digits[d] = 5
				elif len(d & check[2]) == 3:
					digits[d] = 3
				else:
					digits[d] = 2
		# Identify the output
		num = 0
		for o in output:
			num *= 10
			num += digits[o]
		total += num
	return total


print(day08a())
print(day08b())