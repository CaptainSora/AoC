def day16a():
	with open("2015/day16_input.txt", "r") as f:
		sues = f.read().strip().replace(":", "").replace(",", "").split("\n")
	mfcsam = {
		"children": 3,
		"cats": 7,
		"samoyeds": 2,
		"pomeranians": 3,
		"akitas": 0,
		"vizslas": 0,
		"goldfish": 5,
		"trees": 3,
		"cars": 2,
		"perfumes": 1
	}
	for sue in sues:
		num = int(sue.split()[1])
		things = [name for name in sue.split()[2::2]]
		qty = [int(num) for num in sue.split()[3::2]]
		for i in range(len(things)):
			if mfcsam[things[i]] != qty[i]:
				break
		else:
			return num

def day16b():
	with open("2015/day16_input.txt", "r") as f:
		sues = f.read().strip().replace(":", "").replace(",", "").split("\n")
	mfcsam = {
		"children": 3,
		"cats": 7,
		"samoyeds": 2,
		"pomeranians": 3,
		"akitas": 0,
		"vizslas": 0,
		"goldfish": 5,
		"trees": 3,
		"cars": 2,
		"perfumes": 1
	}
	for sue in sues:
		num = int(sue.split()[1])
		things = [name for name in sue.split()[2::2]]
		qty = [int(num) for num in sue.split()[3::2]]
		for i in range(len(things)):
			if things[i] in ["cats", "trees"]:
				if mfcsam[things[i]] >= qty[i]:
					break
			elif things[i] in ["pomeranians", "goldfish"]:
				if mfcsam[things[i]] <= qty[i]:
					break
			else:
				if mfcsam[things[i]] != qty[i]:
					break
		else:
			return num


print(day16a())
print(day16b())
