def day12a():
	with open("2021/day12_input.txt", "r") as f:
		connections = f.read().strip().split("\n")
	# Create dictionary of cave connections
	conn_dict = {}
	for conn in connections:
		start, end = conn.split("-")
		if start not in conn_dict:
			conn_dict[start] = []
		if end not in conn_dict:
			conn_dict[end] = []
		conn_dict[start].append(end)
		conn_dict[end].append(start)
	# Graph search
	stack = [("start", set(["start"]))]
	n_paths = 0
	while stack:
		cur, visited = stack.pop()
		if cur == "end":
			n_paths += 1
			continue
		possible = [dest for dest in conn_dict[cur] if dest not in visited]
		for p in possible:
			stack.append((p, visited | {p} if p.islower() else visited))
	return n_paths

def day12b():
	with open("2021/day12_input.txt", "r") as f:
		connections = f.read().strip().split("\n")
	# Create dictionary of cave connections
	conn_dict = {}
	for conn in connections:
		start, end = conn.split("-")
		if start not in conn_dict:
			conn_dict[start] = []
		if end not in conn_dict:
			conn_dict[end] = []
		conn_dict[start].append(end)
		if start != "start":
			conn_dict[end].append(start)
	# Graph search
	stack = [("start", set(), False)]
	n_paths = 0
	while stack:
		cur, visited, doubled = stack.pop()
		if cur == "end":
			n_paths += 1
			continue
		possible = [
			dest for dest in conn_dict[cur]
			if not doubled or dest not in visited
		]
		for p in possible:
			doubling = p in visited
			stack.append((
				p,
				visited | {p} if p.islower() else visited,
				doubled or doubling
			))
	return n_paths


print(day12a())
print(day12b())
