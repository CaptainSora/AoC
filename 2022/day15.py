def day15a():
	with open("2022/day15_input.txt", "r") as f:
		source = f.read().strip().replace(",", "").replace(":", "") \
			.replace("=", " ").strip().split("\n")
	no_beacon = set()
	yrow = 2000000
	for line in source:
		line = line.split()
		sx, sy, bx, by = [int(line[idx]) for idx in [3, 5, 11, 13]]
		d = abs(sx - bx) + abs(sy - by)
		width = d - abs(sy - yrow)
		if width > 0:
			no_beacon.update(list(range(sx - width, sx + width + 1)))
	no_beacon.discard(yrow)
	return len(no_beacon)
	
# A lil slow, about 30s
def day15b():
	with open("2022/day15_input.txt", "r") as f:
		source = f.read().strip().replace(",", "").replace(":", "") \
			.replace("=", " ").strip().split("\n")
	sensors = []
	for line in source:
		line = line.split()
		sx, sy, bx, by = [int(line[idx]) for idx in [3, 5, 11, 13]]
		sensors.append([sx, sy, abs(sx - bx) + abs(sy - by)])
	for y in range(4000001):
		x = 0
		while x <= 4000000:
			for s in sensors:
				if abs(x - s[0]) + abs(y - s[1]) <= s[2]:
					x = s[0] + s[2] - abs(y - s[1]) + 1
					break
			else:
				return x * 4000000 + y



print(day15a())
print(day15b())
