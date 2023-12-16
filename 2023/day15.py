def day15a():
	with open("2023/day15_input.txt", "r") as f:
		algo = f.read().strip().split(",")
	total_value = 0
	for line in algo:
		value = 0
		for char in line:
			value = ((value + ord(char)) * 17) % 256
		total_value += value
	return total_value


def day15b():
	with open("2023/day15_input.txt", "r") as f:
		algo = f.read().strip().split(",")
	boxes = [{} for _ in range(256)]
	for line in algo:
		boxnum = 0
		pos = max(line.find("="), line.find("-"))
		label, instr = line[:pos], line[pos:]
		for char in label:
			boxnum = ((boxnum + ord(char)) * 17) % 256
		if instr[0] == "=":
			boxes[boxnum][label] = int(instr[1])
		elif instr[0] == "-":
			boxes[boxnum].pop(label, None)
	
	total_power = 0
	for idx, box in enumerate(boxes, start=1):
		slot = 1
		for label, flen in box.items():
			total_power += idx * slot * flen
			slot += 1

	return total_power


print(day15a())
print(day15b())
