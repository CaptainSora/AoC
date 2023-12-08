from itertools import cycle
from math import lcm


def day08a():
	with open("2023/day08_input.txt", "r") as f:
		dirs, maps = f.read().strip().split("\n\n")
	pos = "AAA"
	steps = 0
	network_dict = {}
	maps = maps.replace("(", "").replace(")", "").replace(",", "").split("\n")
	for line in maps:
		line = line.split()
		network_dict[line[0]] = [line[2], line[3]]
	for d in cycle(dirs):
		if pos == "ZZZ":
			return steps
		pos = network_dict[pos]["LR".index(d)]
		steps += 1

	

def day08b():
	with open("2023/day08_input.txt", "r") as f:
		dirs, maps = f.read().strip().split("\n\n")
	pos_group = []
	steps_group = []
	network_dict = {}
	maps = maps.replace("(", "").replace(")", "").replace(",", "").split("\n")
	for line in maps:
		line = line.split()
		network_dict[line[0]] = [line[2], line[3]]
		if line[0][2] == "A":
			pos_group.append(line[0])
	for pos in pos_group:
		steps = 0
		for d in cycle(dirs):
			if pos[2] == "Z":
				steps_group.append(steps)
				break
			pos = network_dict[pos]["LR".index(d)]
			steps += 1
	return lcm(*steps_group)


print(day08a())
print(day08b())
