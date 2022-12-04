def day22a():
	with open("2020/day22_input.txt", "r") as f:
		p1, p2 = f.read().strip().split('\n\n')
	p1 = [int(num) for num in p1.split('\n')[1:]]
	p2 = [int(num) for num in p2.split('\n')[1:]]

	while p1 and p2:
		c1 = p1.pop(0)
		c2 = p2.pop(0)
		if c1 > c2:
			p1.append(c1)
			p1.append(c2)
		elif c2 > c1:
			p2.append(c2)
			p2.append(c1)
		else:
			print("Tie!")
			return -1
	final = p1 + p2
	return sum([final[i] * (len(final) - i) for i in range(len(final))])

def day22b():
	with open("2020/day22_input.txt", "r") as f:
		p1, p2 = f.read().strip().split('\n\n')
	p1 = [int(num) for num in p1.split('\n')[1:]]
	p2 = [int(num) for num in p2.split('\n')[1:]]
	prev = []

	def recursive_combat(p1, p2):
		# Returns False if p1 wins, True if p2 wins
		prev = []
		while p1 and p2:
			state = [p1[:], p2[:]]
			if state in prev:
				return False # p1 instant win
			prev.append(state)
			c1 = p1.pop(0)
			c2 = p2.pop(0)
			if c1 <= len(p1) and c2 <= len(p2):
				result = recursive_combat(p1[:c1], p2[:c2])
			else: # standard
				result = c1 < c2
			if not result: # p1 wins
				p1.append(c1)
				p1.append(c2)
			else:
				p2.append(c2)
				p2.append(c1)
		if p1:
			return False # p1 wins
		else:
			return True

	while p1 and p2:
		state = [p1[:], p2[:]]
		if state in prev:
			break
		prev.append(state)
		c1 = p1.pop(0)
		c2 = p2.pop(0)
		if c1 <= len(p1) and c2 <= len(p2):
			result = recursive_combat(p1[:c1], p2[:c2])
		else: # standard
			result = c1 < c2
		if not result: # False = p1 wins
			p1.append(c1)
			p1.append(c2)
		else:
			p2.append(c2)
			p2.append(c1)
	final = p1 + p2
	return sum([final[i] * (len(final) - i) for i in range(len(final))])


print(day22a())
print(day22b())
