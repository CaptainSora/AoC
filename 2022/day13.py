from json import loads


class Packet:
	def __init__(self, obj):
		self.obj = obj
	
	def lstcmp(self, other):
		"""
		Requires self.obj and other.obj to be lists
		Returns a 3-way comparison like cmp()
		"""
		if not self.obj and not other.obj:
			return 0
		elif not self.obj:
			return -1
		elif not other.obj:
			return 1
		
		first = Packet(self.obj[0]).cmp(Packet(other.obj[0]))
		if first != 0:
			return first
		return Packet(self.obj[1:]).lstcmp(Packet(other.obj[1:]))

	def cmp(self, other):
		"""
		self.obj, other.obj: Anyof(Int, List)
		Returns a 3-way comparison:
		-1: self.obj < other.obj
		0: self.obj = other.obj
		1: self.obj > other.obj
		"""
		if type(self.obj) is int:
			if type(other.obj) is int:
				return (self.obj > other.obj) - (self.obj < other.obj)
			else:
				return Packet([self.obj]).cmp(other)
		else:
			if type(other.obj) is int:
				return self.cmp(Packet([other.obj]))
			else:
				return self.lstcmp(other)
	
	def __lt__(self, other):
		return self.cmp(other) == -1


def day13a():
	with open("2022/day13_input.txt", "r") as f:
		packets = [
			idx for idx, line in enumerate(f.read().split("\n\n"), 1)
			if Packet(loads(line.split()[0])) < Packet(loads(line.split()[1]))
		]
	return sum(packets)

def day13b():
	with open("2022/day13_input.txt", "r") as f:
		packets = [
			Packet(loads(line)) for line in f.read().split("\n") if line
		]
	dividers = [Packet([[2]]), Packet([[6]])]
	packets.extend(dividers)
	packets.sort()
	return (packets.index(dividers[0]) + 1) * (packets.index(dividers[1]) + 1)


print(day13a())
print(day13b())
