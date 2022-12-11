def day23a():
	with open("2015/day23_input.txt", "r") as f:
		instr = f.read().replace(",", "").strip().split("\n")
	reg = {"a": 0, "b": 0}
	offset = 0
	while offset >= 0 and offset < len(instr):
		line = instr[offset].split()
		if line[0] == "hlf":
			reg[line[1]] //= 2
		elif line[0] == "tpl":
			reg[line[1]] *= 3
		elif line[0] == "inc":
			reg[line[1]] += 1
		elif line[0] == "jmp":
			offset += int(line[1]) - 1
		elif line[0] == "jie":
			if reg[line[1]] % 2 == 0:
				offset += int(line[2]) - 1
		elif line[0] == "jio":
			if reg[line[1]] == 1:
				offset += int(line[2]) - 1
		offset += 1
	return reg["b"]


def day23b():
	with open("2015/day23_input.txt", "r") as f:
		instr = f.read().replace(",", "").strip().split("\n")
	reg = {"a": 1, "b": 0}
	offset = 0
	while offset >= 0 and offset < len(instr):
		line = instr[offset].split()
		if line[0] == "hlf":
			reg[line[1]] //= 2
		elif line[0] == "tpl":
			reg[line[1]] *= 3
		elif line[0] == "inc":
			reg[line[1]] += 1
		elif line[0] == "jmp":
			offset += int(line[1]) - 1
		elif line[0] == "jie":
			if reg[line[1]] % 2 == 0:
				offset += int(line[2]) - 1
		elif line[0] == "jio":
			if reg[line[1]] == 1:
				offset += int(line[2]) - 1
		offset += 1
	return reg["b"]


print(day23a())
print(day23b())
