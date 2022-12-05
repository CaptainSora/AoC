def day02a():
	with open("2015/day02_input.txt", "r") as f:
		dims = f.read().strip().split("\n")
	paper = 0
	for d in dims:
		l, w, h = sorted([int(num) for num in d.split("x")])
		paper += 2 * (l*w + w*h + h*l) + l*w
	return paper

def day02b():
	with open("2015/day02_input.txt", "r") as f:
		dims = f.read().strip().split("\n")
	ribbon = 0
	for d in dims:
		l, w, h = sorted([int(num) for num in d.split("x")])
		ribbon += 2 * (l + w) + l*w*h
	return ribbon


print(day02a())
print(day02b())
