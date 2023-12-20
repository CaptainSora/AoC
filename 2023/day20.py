from itertools import count
from math import lcm


class Node:
	def __init__(self, mod_type, name, dests):
		# One of %, &, b
		self.type = mod_type
		self.name = name
		# Inputs and outputs
		self.src = {}
		self.dest = dests.split(", ")
		self.state = False
	
	def add_src(self, name):
		self.src[name] = False

	def pulse(self, high, src):
		match self.type:
			case "b":
				return self.send(high)
			case "%" if not high:
				self.state = not self.state
				return self.send(self.state)
			case "&":
				self.src[src] = high
				mem = [v for _, v in self.src.items()]
				return self.send(not all(mem))
			case _:
				return []
	
	def send(self, ptype):
		return [[ptype, d, self.name] for d in self.dest]


def day20a():
	with open("2023/day20_input.txt", "r") as f:
		node_list = f.read().strip().split("\n")
	nodes = {}
	# Initialize nodes
	for line in node_list:
		node, dests = line.split(" -> ")
		nodes[node[1:]] = Node(node[0], node[1:], dests)
	# Add sources
	for line in node_list:
		node, dests = line.split(" -> ")
		src = node[1:]
		for d in dests.split(", "):
			if d in nodes:
				nodes[d].add_src(src)
	# Push button go boom
	npulses = [0, 0]
	for i in range(1000):
		npulses[0] += 1
		transit = nodes["roadcaster"].pulse(False, None)
		while transit:
			ptype, dest, src = transit.pop(0)
			npulses[int(ptype)] += 1
			if dest not in nodes:
				continue
			transit.extend(nodes[dest].pulse(ptype, src))
	return npulses[0] * npulses[1]


def day20b():
	with open("2023/day20_input.txt", "r") as f:
		node_list = f.read().strip().split("\n")
	nodes = {}
	# Initialize nodes
	for line in node_list:
		node, dests = line.split(" -> ")
		nodes[node[1:]] = Node(node[0], node[1:], dests)
	# Add new node
	nodes["rx"] = Node(None, "rx", "")
	# Add sources
	for line in node_list:
		node, dests = line.split(" -> ")
		src = node[1:]
		for d in dests.split(", "):
			if d in nodes:
				nodes[d].add_src(src)
	# Push button go boom
	noted = nodes["vr"].src
	cycles = []
	for i in count(1):
		if len(cycles) >= len(noted):
			return lcm(*cycles)
		transit = nodes["roadcaster"].pulse(False, None)
		while transit:
			ptype, dest, src = transit.pop(0)
			if dest not in nodes:
				continue
			elif src in noted and ptype:
				cycles.append(i)
			transit.extend(nodes[dest].pulse(ptype, src))


print(day20a())
print(day20b())
