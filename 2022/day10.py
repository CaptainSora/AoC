def day10a():
	with open("2022/day10_input.txt", "r") as f:
		cmd = f.read().strip().split("\n")
	signal = 0
	x = 1
	cycles = [20, 60, 100, 140, 180, 220]
	cycle = 1

	def tick():
		nonlocal cycle, signal, x
		cycle += 1
		if cycle in cycles:
			signal += x * cycle
	
	for instr in cmd:
		instr = instr.split()
		if instr[0] == "addx":
			tick()
			x += int(instr[1])
		tick()
	return signal

def day10b():
	with open("2022/day10_input.txt", "r") as f:
		cmd = f.read().strip().split("\n")
	x = 1
	cycle = 0
	screen = [["." for _ in range(40)] for _ in range(6)]

	def tick():
		nonlocal cycle, screen, x
		cycle += 1
		r, c = divmod(cycle, 40)
		if abs(c - x) <= 1:
			screen[r][c] = "#"
	
	for instr in cmd:
		instr = instr.split()
		if instr[0] == "addx":
			tick()
			x += int(instr[1])
		tick()
	return "\n".join(["".join(row) for row in screen])


print(day10a())
print(day10b())
