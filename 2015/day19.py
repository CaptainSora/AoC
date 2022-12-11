from queue import PriorityQueue


def day19a():
	with open("2015/day19_input.txt", "r") as f:
		repl_list, molecule = f.read().split("\n\n")
	repl = {}
	for line in repl_list.strip().split("\n"):
		src, prod = line.split(" => ")
		if src not in repl:
			repl[src] = []
		repl[src].append(prod)
	synth = set()
	for k, v in repl.items():
		start = molecule.find(k)
		while start > -1:
			for m in v:
				synth.add(molecule[:start] + m + molecule[start+len(k):])
			start = molecule.find(k, start+1)
	return len(synth)

def day19b():
	with open("2015/day19_input.txt", "r") as f:
		repl_list, source = f.read().split("\n\n")
	repl = {}
	final = []
	for line in repl_list.strip().split("\n"):
		src, prod = line.split(" => ")
		if src == "e":
			final.append(prod)
		else:
			repl[prod] = src
	seen = set()
	q = PriorityQueue()
	q.put_nowait((len(source), 0, source))
	while not q.empty():
		(_, steps, molecule) = q.get_nowait()
		for k, v in repl.items():
			start = molecule.find(k)
			while start > -1:
				fab = molecule[:start] + v + molecule[start+len(k):]
				if fab in final:
					return steps + 1
				if fab not in seen:
					seen.add(fab)
					q.put_nowait((len(fab), steps+1, fab))
				start = molecule.find(k, start+1)


print(day19a())
print(day19b())
