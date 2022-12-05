def day05a():
	with open("2022/day05_input.txt", "r") as f:
		stack, instr = f.read().split("\n\n")
	# Isolate and transpose
	stack = list(zip(*[
		[line[i+1] for i in range(0, len(line), 4)]
		for line in stack.split("\n")[:-1]
	]))
	# Reverse (lowest at 0) and drop blanks
	stack = [list(''.join(s[::-1]).strip()) for s in stack]

	for line in instr.strip().split("\n"):
		_, q, _, frm, _, to = line.split()
		q, frm, to = int(q), int(frm) - 1, int(to) - 1
		for _ in range(q):
			stack[to].append(stack[frm].pop())
	return ''.join([s[-1] for s in stack])

def day05b():
	with open("2022/day05_input.txt", "r") as f:
		stack, instr = f.read().split("\n\n")
	# Isolate and transpose
	stack = list(zip(*[
		[line[i+1] for i in range(0, len(line), 4)]
		for line in stack.split("\n")[:-1]
	]))
	# Reverse (lowest at 0) and drop blanks
	stack = [list(''.join(s[::-1]).strip()) for s in stack]

	for line in instr.strip().split("\n"):
		_, q, _, frm, _, to = line.split()
		q, frm, to = int(q), int(frm) - 1, int(to) - 1
		stack[to].extend(stack[frm][-q:])
		stack[frm] = stack[frm][:-q]
	return ''.join([s[-1] for s in stack])


print(day05a())
print(day05b())
