def day07a():
	with open("2022/day07_input.txt", "r") as f:
		cmd = f.read().strip().split("\n")
	dirs = {".": 0}
	cur = []
	for c in cmd:
		c = c.strip().split()
		if c[0] == "$":
			if c[1] == "cd":
				if c[2] == "/":
					cur = ["."]
				elif c[2] == "..":
					cur.pop()
				else:
					cur.append(c[2])
					p = "/".join(cur)
					if p not in dirs:
						dirs[p] = 0
			elif c[1] == "ls":
				pass
		elif c[0] == "dir":
			pass
		else:
			for i in range(len(cur)):
				p = "/".join(cur[:i+1])
				dirs[p] += int(c[0])
	return sum([v for k, v in dirs.items() if v <= 100000])

def day07b():
	with open("2022/day07_input.txt", "r") as f:
		cmd = f.read().strip().split("\n")
	dirs = {".": 0}
	cur = []
	for c in cmd:
		c = c.strip().split()
		if c[0] == "$":
			if c[1] == "cd":
				if c[2] == "/":
					cur = ["."]
				elif c[2] == "..":
					cur.pop()
				else:
					cur.append(c[2])
					p = "/".join(cur)
					if p not in dirs:
						dirs[p] = 0
			elif c[1] == "ls":
				pass
		elif c[0] == "dir":
			pass
		else:
			for i in range(len(cur)):
				p = "/".join(cur[:i+1])
				dirs[p] += int(c[0])
	needed = 30000000 - (70000000 - dirs["."])
	return sorted([v for k, v in dirs.items() if v >= needed])[0]


print(day07a())
print(day07b())
