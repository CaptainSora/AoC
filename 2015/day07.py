from collections import deque


def day07a():
	with open("2015/day07_input.txt", "r") as f:
		instr = deque(f.read().strip().split("\n"))
	signals = {}

	def retrieve(value):
		if value.isdigit():
			return int(value)
		else:
			return signals[value]

	while "a" not in signals:
		raw_input, output = instr.popleft().split(" -> ")
		input = raw_input.split()
		try:
			if len(input) == 1:
				signals[output] = retrieve(input[0])
			elif len(input) == 2:
				signals[output] = ~ retrieve(input[1])
			elif input[1] == "AND":
				signals[output] = retrieve(input[0]) & retrieve(input[2])
			elif input[1] == "OR":
				signals[output] = retrieve(input[0]) | retrieve(input[2])
			elif input[1] == "LSHIFT":
				signals[output] = retrieve(input[0]) << retrieve(input[2])
			elif input[1] == "RSHIFT":
				signals[output] = retrieve(input[0]) >> retrieve(input[2])
			else:
				print(raw_input, output)
				raise ValueError("Instructions not caught")
		except KeyError:
			instr.append(raw_input + " -> " + output)
	return signals["a"]

def day07b():
	with open("2015/day07_input.txt", "r") as f:
		instr = deque(f.read().strip().split("\n"))
	signals = {"b": day07a()}

	def retrieve(value):
		if value.isdigit():
			return int(value)
		else:
			return signals[value]

	while "a" not in signals:
		raw_input, output = instr.popleft().split(" -> ")
		if output == "b": # Override
			continue
		input = raw_input.split()
		try:
			if len(input) == 1:
				signals[output] = retrieve(input[0])
			elif len(input) == 2:
				signals[output] = ~ retrieve(input[1])
			elif input[1] == "AND":
				signals[output] = retrieve(input[0]) & retrieve(input[2])
			elif input[1] == "OR":
				signals[output] = retrieve(input[0]) | retrieve(input[2])
			elif input[1] == "LSHIFT":
				signals[output] = retrieve(input[0]) << retrieve(input[2])
			elif input[1] == "RSHIFT":
				signals[output] = retrieve(input[0]) >> retrieve(input[2])
			else:
				print(raw_input, output)
				raise ValueError("Instructions not caught")
		except KeyError:
			instr.append(raw_input + " -> " + output)
	return signals["a"]


print(day07a())
print(day07b())
