def day14a():
	with open("2020/day14_input.txt", "r") as f:
		instructions = [
			eq.strip().split(' = ') for eq in f.read().strip().split('\n')]
	
	mask = ""
	memory = {}

	def add_mask(value):
		result = ""
		for i in range(len(mask)):
			if mask[i] == "X":
				result += value[i]
			else:
				result += mask[i]
		return int(result, 2)
	
	for instr in instructions:
		if instr[0] == "mask":
			mask = instr[1]
		else:
			location = int(instr[0][4:-1])
			value = f"{int(instr[1]):036b}"
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
		result = ""
		for i in range(len(mask)):
			if mask[i] == "0":
				result += location[i]
			else:
				result += mask[i]
		
		xcount = result.count("X")
		for i in range(2**xcount):
			adj = f"{i:b}"
			while len(adj) < xcount:
				adj = "0" + adj
			c = 0
			newvalue = ""
			for char in result:
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
			location = f"{int(instr[0][4:-1]):036b}"
			value = int(instr[1])
			add_mask(location, value)
	return sum(memory.values())


print(day14a())
print(day14b())
