def day10a():
	with open("2021/day10_input.txt", "r") as f:
		navsys = f.read().strip().split("\n")
	errorscore = 0
	for line in navsys:
		chunk = []
		for chr in line:
			if chr in "([{<":
				chunk.append(chr)
			else:
				idx = ")]}>".index(chr)
				if chunk[-1] != "([{<"[idx]:
					errorscore += [3, 57, 1197, 25137][idx]
					break
				chunk.pop()
	return errorscore

def day10b():
	with open("2021/day10_input.txt", "r") as f:
		navsys = f.read().strip().split("\n")
	compscore = []
	for line in navsys:
		chunk = []
		for chr in line:
			if chr in "([{<":
				chunk.append(chr)
			else:
				idx = ")]}>".index(chr)
				if chunk[-1] != "([{<"[idx]:
					break
				chunk.pop()
		else:
			score = 0
			while chunk:
				score *= 5
				score += "([{<".index(chunk.pop()) + 1
			compscore.append(score)
	return sorted(compscore)[len(compscore)//2]


print(day10a())
print(day10b())
