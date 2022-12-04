# Takes awhile, deprecated
def day19ax():
	with open("2020/day19_input.txt", "r") as f:
		rules, messages = f.read().strip().split('\n\n')
	rules = [[int(row.split(": ")[0]), row.split(": ")[1]]
		for row in rules.split('\n')]
	rules.sort()
	rules = [[[int(num) if num.isdigit() else num[1] for num in sec.split(" ")]
		for sec in row[1].split(" | ")]
		for row in rules]
	messages = messages.split('\n')

	def replace(numlist):
		ret1 = []
		ret2 = []
		replaced = False
		split = False
		# replaces the first number in the list
		for num in numlist:
			if replaced or isinstance(num, str):
				ret1.append(num)
				ret2.append(num)
			else:
				replaced = True
				rule = rules[num]
				ret1 += rule[0]
				if len(rule) == 1:
					ret2 += rule[0]
				else:
					split = True
					ret2 += rule[1]
		if split:
			return [ret1, ret2]
		else:
			return [ret1]

	inprogress = [[0]]
	valid = []
	while len(inprogress) > 0:
		numlist = inprogress.pop()
		next = replace(numlist)
		for nums in next:
			if all([isinstance(c, str) for c in nums]):
				valid.append(''.join(nums))
			else:
				inprogress.append(nums)
	
	return sum([m in valid for m in messages])

# Modified version of part 2, very fast
def day19a():
	with open("2020/day19_input.txt", "r") as f:
		rules, messages = f.read().strip().split('\n\n')
	rules = [[int(row.split(": ")[0]), row.split(": ")[1]]
		for row in rules.split('\n')]
	rules.sort()
	rules = [[[int(num) if num.isdigit() else num[1] for num in sec.split(" ")]
		for sec in row[1].split(" | ")]
		for row in rules]
	messages = messages.split('\n')

	def replace(numlist):
		ret1 = []
		ret2 = []
		replaced = False
		split = False
		# replaces the first number in the list
		for num in numlist:
			if replaced or isinstance(num, str):
				ret1.append(num)
				ret2.append(num)
			else:
				replaced = True
				rule = rules[num]
				ret1 += rule[0]
				if len(rule) == 1:
					ret2 += rule[0]
				else:
					split = True
					ret2 += rule[1]
		if split:
			return [ret1, ret2]
		else:
			return [ret1]

	inprogress = [[42]]
	valid42 = []
	while len(inprogress) > 0:
		numlist = inprogress.pop()
		next = replace(numlist)
		for nums in next:
			if all([isinstance(c, str) for c in nums]):
				valid42.append(''.join(nums))
			else:
				inprogress.append(nums)
	
	inprogress = [[31]]
	valid31 = []
	while len(inprogress) > 0:
		numlist = inprogress.pop()
		next = replace(numlist)
		for nums in next:
			if all([isinstance(c, str) for c in nums]):
				valid31.append(''.join(nums))
			else:
				inprogress.append(nums)
	
	counter = 0
	for m in messages:
		if len(m) != 24:
			continue
		if m[:8] in valid42 and m[8:16] in valid42 and m[16:] in valid31:
			counter += 1
	
	return counter

# Very fast
def day19b():
	with open("2020/day19_input.txt", "r") as f:
		rules, messages = f.read().strip().split('\n\n')
	rules = [[int(row.split(": ")[0]), row.split(": ")[1]]
		for row in rules.split('\n')]
	rules.sort()
	rules = [[[int(num) if num.isdigit() else num[1] for num in sec.split(" ")]
		for sec in row[1].split(" | ")]
		for row in rules]
	messages = messages.split('\n')

	def replace(numlist):
		ret1 = []
		ret2 = []
		replaced = False
		split = False
		# replaces the first number in the list
		for num in numlist:
			if replaced or isinstance(num, str):
				ret1.append(num)
				ret2.append(num)
			else:
				replaced = True
				rule = rules[num]
				ret1 += rule[0]
				if len(rule) == 1:
					ret2 += rule[0]
				else:
					split = True
					ret2 += rule[1]
		if split:
			return [ret1, ret2]
		else:
			return [ret1]

	inprogress = [[42]]
	valid42 = []
	while len(inprogress) > 0:
		numlist = inprogress.pop()
		next = replace(numlist)
		for nums in next:
			if all([isinstance(c, str) for c in nums]):
				valid42.append(''.join(nums))
			else:
				inprogress.append(nums)
	
	inprogress = [[31]]
	valid31 = []
	while len(inprogress) > 0:
		numlist = inprogress.pop()
		next = replace(numlist)
		for nums in next:
			if all([isinstance(c, str) for c in nums]):
				valid31.append(''.join(nums))
			else:
				inprogress.append(nums)
	
	counter = 0
	for m in messages:
		if len(m) % 8 != 0:
			continue
		switch = False
		success = True
		c42 = 0
		c31 = 0
		for i in range(int(len(m)/8)):
			teststr = m[8 * i : 8 * (i+1)]
			if not switch:
				if teststr in valid42:
					c42 += 1
					continue
				else:
					switch = True
			if switch:
				if teststr in valid31:
					c31 += 1
				else:
					success = False
					break
		if success and c42 > c31 and c31 > 0:
			counter += 1
	
	return counter


print(day19a())
print(day19b())
