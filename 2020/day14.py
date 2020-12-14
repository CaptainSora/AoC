def day14a():
	with open("2020/day14_input.txt", "r") as f:
		instructions = [
			eq.strip().split(' = ') for eq in f.read().strip().split('\n')]
	
	mask = ""
	memory = {}

	def add_mask(value):
		retval = ""
		for i in range(len(mask)):
			if mask[i] == "X":
				retval += value[i]
			else:
				retval += mask[i]
		return int(retval, 2)
	
	for instr in instructions:
		if instr[0] == "mask":
			mask = instr[1]
		else:
			location = int(instr[0][4:-1])
			value = f"{int(instr[1]):b}"
			while len(value) < 36:
				value = "0" + value
			memory[location] = add_mask(value)
	
	return sum(memory.values())
	

def day14b():
	with open("2020/day14_input.txt", "r") as f:
		instructions = [
			eq.strip().split(' = ') for eq in f.read().strip().split('\n')]
	
	mask = ""
	memory = {}

	def add_mask(location, value):
		nonlocal memory
		retval = ""
		for i in range(len(mask)):
			if mask[i] == "0":
				retval += location[i]
			else:
				retval += mask[i]
		
		xcount = retval.count("X")
		for i in range(2**xcount):
			adj = f"{i:b}"
			while len(adj) < xcount:
				adj = "0" + adj
			c = 0
			newvalue = ""
			for char in retval:
				if char == "X":
					newvalue += adj[c]
					c += 1
				else:
					newvalue += char
			memory[int(newvalue, 2)] = value
	
	for instr in instructions:
		if instr[0] == "mask":
			mask = instr[1]
		else:
			location = f"{int(instr[0][4:-1]):b}"
			value = int(instr[1])
			while len(location) < 36:
				location = "0" + location
			add_mask(location, value)
	return sum(memory.values())

print(day14b())
