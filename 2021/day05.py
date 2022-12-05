from math import copysign


def day05a():
	with open("2021/day05_input.txt", "r") as f:
		vents = f.read().strip().split("\n")
	danger = {}
	for vent in vents:
		x1, y1, x2, y2 = [
			int(num) for num in vent.replace(" -> ", ",").split(",")]
		if x1 == x2:
			start, stop = min(y1, y2), max(y1, y2) + 1
		elif y1 == y2: # Assumed y1 == y2
			start, stop = min(x1, x2), max(x1, x2) + 1
		else:
			continue
		for i in range(start, stop):
			if x1 == x2:
				loc = (x1, i)
			else:
				loc = (i, y1)
			# Trying EAFP style instead of LBYL
			try:
				danger[loc] += 1
			except KeyError:
				danger[loc] = 1
	return len([k for k, v in danger.items() if v >= 2])

def day05b():
	with open("2021/day05_input.txt", "r") as f:
		vents = f.read().strip().split("\n")
	danger = {}
	for vent in vents:
		x1, y1, x2, y2 = [
			int(num) for num in vent.replace(" -> ", ",").split(",")]
		if x1 == x2:
			start, stop = min(y1, y2), max(y1, y2) + 1
		elif y1 == y2: # Assumed y1 == y2
			start, stop = min(x1, x2), max(x1, x2) + 1
		else:
			start, stop = 0, abs(x2 - x1) + 1
			xdir, ydir = copysign(1, x2 - x1), copysign(1, y2 - y1)
		for i in range(start, stop):
			if x1 == x2:
				loc = (x1, i)
			elif y1 == y2:
				loc = (i, y1)
			else:
				loc = (x1 + i * xdir, y1 + i * ydir)
			# Trying EAFP style instead of LBYL
			try:
				danger[loc] += 1
			except KeyError:
				danger[loc] = 1
	return len([k for k, v in danger.items() if v >= 2])


print(day05a())
print(day05b())
