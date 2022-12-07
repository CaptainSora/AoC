def day11a(input=None):
	if input is None:
		input = "hxbxwxba"
	pwd = [(ord(input[i]) - 96) for i in range(len(input))]
	pwd[-1] += 1
	while True:
		# Carry-over
		for i in range(1, len(input)):
			if pwd[-i] == 27:
				pwd[-i] = 1
				pwd[-i-1] += 1
			else:
				break
		### Check conditions
		# Banned letters
		try:
			idx = min(pwd.index(9), pwd.index(12), pwd.index(15))
		except ValueError:
			pass
		else:
			pwd[idx] += 1
			continue
		# Straight
		for i in range(2, len(input)):
			if pwd[i-2] + 1 == pwd[i-1] and pwd[i-1] + 1 == pwd[i]:
				break
		else:
			pwd[-1] += 1
			continue
		# Two doubles
		doubles = []
		for i in range(1, len(input)):
			if pwd[i-1] == pwd[i]:
				doubles.append(pwd[i])
		if len(set(doubles)) < 2:
			pwd[-1] += 1
			continue
		# All pass
		return ''.join([chr(d + 96) for d in pwd])


def day11b():
	input = day11a()
	return day11a(input=input)


print(day11a())
print(day11b())
