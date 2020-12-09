def day09a():
	with open("2020/day09_input.txt", "r") as f:
		xmas = [int(num) for num in f.read().strip().split('\n')]
	
	for i in range(25, len(xmas)):
		target = xmas[i]
		found = False
		for j in xmas[i-25:i]:
			if target - j in xmas[i-25:i]:
				found = True
				break
		if not found:
			return xmas[i]

def day09b():
	with open("2020/day09_input.txt", "r") as f:
		xmas = [int(num) for num in f.read().strip().split('\n')]
	
	invalid = 0
	for i in range(25, len(xmas)):
		target = xmas[i]
		found = False
		for j in xmas[i-25:i]:
			if target - j in xmas[i-25:i]:
				found = True
				break
		if not found:
			invalid = xmas[i]
			break
	
	length = 2
	while True:
		for i in range(len(xmas) - length + 1):
			contig = xmas[i:i+length]
			if sum(contig) == invalid:
				return min(contig) + max(contig)
		length += 1

print(day09b())
