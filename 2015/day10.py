def day10a():
	input = "1113222113"
	output = ""
	for _ in range(40):
		prev = input[0]
		for d in input[1:]:
			if d != prev[-1]:
				output += str(len(prev)) + prev[0]
				prev = d
			else:
				prev += d
		if prev:
			output += str(len(prev)) + prev[0]
		input, output = output, ""
	return len(input)

def day10b():
	input = "1113222113"
	output = ""
	for _ in range(50):
		prev = input[0]
		for d in input[1:]:
			if d != prev[-1]:
				output += str(len(prev)) + prev[0]
				prev = d
			else:
				prev += d
		if prev:
			output += str(len(prev)) + prev[0]
		input, output = output, ""
	return len(input)


print(day10a())
print(day10b())
