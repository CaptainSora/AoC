def valid(value, rules):
	for rule in rules:
		for rangepos in rule:
			if value >= rangepos[0] and value <= rangepos[1]:
				return True
	return False

def day16a():
	with open("2020/day16_input.txt", "r") as f:
		rules, myticket, othertickets = f.read().strip().split('\n\n')
	rules = [[[int(num) for num in r.strip().split('-')]
		for r in row.split(': ')[1].split(' or ')]
		for row in rules.split('\n')]
	othertickets = [[int(num) for num in row.split(',')]
		for row in othertickets.strip().split('\n')[1:]]
	
	errorrate = 0
	for t in othertickets:
		validity = [valid(num, rules) for num in t]
		for i in range(len(validity)):
			if not validity[i]:
				errorrate += t[i]
	
	return errorrate


def valid2(value, rules):
	validlist = []
	for rule in rules:
		rulevalid = False
		for rangepos in rule:
			if value >= rangepos[0] and value <= rangepos[1]:
				rulevalid = True
				break
		validlist.append(rulevalid)
	return validlist


def day16b():
	with open("2020/day16_input.txt", "r") as f:
		rules, myticket, othertickets = f.read().strip().split('\n\n')
	rules = [[[int(num) for num in r.strip().split('-')]
		for r in row.split(': ')[1].split(' or ')]
		for row in rules.split('\n')]
	myticket = [int(num) for num in myticket.split('\n')[1].split(',')]
	othertickets = [[int(num) for num in row.split(',')]
		for row in othertickets.strip().split('\n')[1:]]
	
	validtickets = []
	
	for t in othertickets:
		if all([valid(num, rules) for num in t]):
			validtickets.append(t)
	
	# Valid tickets
	fields = [list(range(len(rules))) for _ in range(len(rules))]
	
	for t in validtickets:
		validity = [valid2(num, rules) for num in t]
		for i in range(len(validity)): # 20
			# i is ticket field position
			for j in range(len(rules)):
				if not validity[i][j] and j in fields[i]:
					fields[i].remove(j)
	finalfields = [-1 for _ in range(len(rules))]
	while -1 in finalfields:
		for i in range(len(fields)):
			if len(fields[i]) == 1 and fields[i][0] not in finalfields:
				num = fields[i][0]
				for j in range(len(fields)):
					if num in fields[j]:
						fields[j].remove(num)
				finalfields[i] = num
	
	fieldprod = 1
	for pos in range(len(finalfields)):
		if finalfields[pos] < 6:
			fieldprod *= myticket[pos]
	
	return fieldprod




print(day16b())
