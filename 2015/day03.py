def day03a():
	with open("2015/day03_input.txt", "r") as f:
		dirs = f.read().strip()
	houses = {(0, 0)} # Set constructor
	x, y = 0, 0
	for d in dirs:
		if d == "^":
			y += 1
		elif d == "v":
			y -= 1
		elif d == "<":
			x -= 1
		elif d == ">":
			x += 1
		houses.add((x, y))
	return len(houses)

def day03b():
	with open("2015/day03_input.txt", "r") as f:
		dirs = f.read().strip()
	houses = {(0, 0)} # Set constructor
	x, y = 0, 0
	prevx, prevy = 0, 0
	for d in dirs:
		if d == "^":
			y += 1
		elif d == "v":
			y -= 1
		elif d == "<":
			x -= 1
		elif d == ">":
			x += 1
		houses.add((x, y))
		x, y, prevx, prevy = prevx, prevy, x, y # SWAP
	return len(houses)


print(day03a())
print(day03b())
