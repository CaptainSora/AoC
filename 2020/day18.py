from math import prod


def day18a():
	with open("2020/day18_input.txt", "r") as f:
		lines = f.read().strip().split('\n')
	total = 0
	for line in lines:
		values = [[0, '+']]
		for c in line:
			if c == " ":
				continue
			elif c.isdigit():
				if values[-1][1] == "+":
					values[-1][0] += int(c)
				else:
					values[-1][0] *= int(c)
			elif c == "(":
				values.append([0, "+"])
			elif c == ")":
				i = values.pop()[0]
				if values[-1][1] == "+":
					values[-1][0] += i
				else:
					values[-1][0] *= i
			else:
				values[-1][1] = c
		total += values[0][0]
	return total

def day18b():
	with open("2020/day18_input.txt", "r") as f:
		lines = [row.replace(" ", "") for row in f.read().strip().split('\n')]
	
	def calc(string):
		# Requires no brackets
		return prod([eval(expr) for expr in string.split("*")])

	total = 0
	for line in lines:
		while True:
			# Find deepest bracket set
			depth = []
			counter = 0
			for c in line:
				if c == "(":
					counter += 1
				elif c == ")":
					counter -= 1
				depth.append(counter)
			if max(depth) == 0:
				break
			start = depth.index(max(depth))
			end = start
			while depth[end] == max(depth):
				end += 1
			value = str(calc(line[start+1:end]))
			line = line[:start] + value + line[end+1:]
		total += calc(line)

	return total


print(day18a())
print(day18b())
