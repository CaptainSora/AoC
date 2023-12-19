from copy import deepcopy
from math import prod


def day19a():
	with open("2023/day19_input.txt", "r") as f:
		wf, parts = f.read().split("\n\n")
	# Parse input
	parts = [
		[int(num) for num in line.split(",")[1::2]]
		for line in parts.replace("}", "").replace("=", ",").strip().split("\n")
	]
	workflows = {}
	for w in wf.replace("}", "").replace("{", ",").strip().split("\n"):
		key, *instr = w.split(",")
		instr[-1] = "True:" + instr[-1]
		workflows[key] = [line.split(":") for line in instr]
	# Sort parts
	a_rtg = 0
	for p in parts:
		x, m, a, s = p
		cur_wf = "in"
		while cur_wf not in "AR":
			for instr, dest in workflows[cur_wf]:
				if eval(instr):
					cur_wf = dest
					break
		if cur_wf == "A":
			a_rtg += sum(p)
	return a_rtg


def day19b():
	with open("2023/day19_input.txt", "r") as f:
		wf, _ = f.read().split("\n\n")
	# Parse input
	workflows = {}
	for w in wf.replace("}", "").replace("{", ",").strip().split("\n"):
		key, *instr = w.split(",")
		instr[-1] = "True:" + instr[-1]
		workflows[key] = [line.split(":") for line in instr]
	# Sort parts
	queue = [["in", [[1, 4000] for _ in range(4)]]]
	a_comb = 0
	while queue:
		wf, xmas = queue.pop()
		# Check wf
		if wf == "A":
			a_comb += prod([rtg[1] - rtg[0] + 1 for rtg in xmas])
			continue
		elif wf == "R":
			continue
		# Process
		for instr, dest in workflows[wf]:
			# Catch end case
			if instr == "True":
				queue.append([workflows[wf][-1][1], xmas])
				break
			# Process as normal
			rtg, op, *val = instr
			val = int("".join(val))
			idx = "xmas".index(rtg)
			xmas_cpy = deepcopy(xmas)
			if op == "<" and val > xmas[idx][0]:
				# Entire block caught
				if val > xmas[idx][1]:
					queue.append([dest, xmas])
					break
				# Partial block caught
				xmas_cpy[idx][1] = val - 1
				xmas[idx][0] = val
				queue.append([dest, xmas_cpy])
			elif op == ">" and val < xmas[idx][1]:
				# Entire block caught
				if val < xmas[idx][0]:
					queue.append([dest, xmas])
					break
				# Partial block caught
				xmas_cpy[idx][0] = val + 1
				xmas[idx][1] = val
				queue.append([dest, xmas_cpy])

	return a_comb


print(day19a())
print(day19b())
