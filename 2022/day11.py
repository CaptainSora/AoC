from collections import deque
from math import prod


class Monkey:
	def __init__(self, infostr):
		info = infostr.strip().replace(",", "").split("\n")
		self.items = deque([int(num) for num in info[1].split()[2:]])
		self.opstr = info[2].split(" = ")[1]
		self.test = int(info[3].split()[-1])
		self.true = int(info[4].split()[-1])
		self.false = int(info[5].split()[-1])
		self.inspected = 0
	
	def inspect(self, worrymod=0):
		# Requires self.items to not be empty
		self.inspected += 1
		old = self.items.popleft()
		old = eval(self.opstr)
		if worrymod:
			old %= worrymod
		else:
			old //= 3
		if old % self.test == 0:
			return self.true, old
		return self.false, old
	
	def __lt__(self, other):
		return self.inspected < other.inspected
		

def day11a():
	with open("2022/day11_input.txt", "r") as f:
		monkeys = [Monkey(block) for block in f.read().split("\n\n")]
	for _ in range(20):
		for i in range(len(monkeys)):
			while monkeys[i].items:
				num, worry = monkeys[i].inspect()
				monkeys[num].items.append(worry)
	monkeys.sort(reverse=True)
	return monkeys[0].inspected * monkeys[1].inspected

def day11b():
	with open("2022/day11_input.txt", "r") as f:
		monkeys = [Monkey(block) for block in f.read().split("\n\n")]
	worrymod = prod([m.test for m in monkeys])
	for _ in range(10000):
		for i in range(len(monkeys)):
			while monkeys[i].items:
				num, worry = monkeys[i].inspect(worrymod=worrymod)
				monkeys[num].items.append(worry)
	monkeys.sort(reverse=True)
	return monkeys[0].inspected * monkeys[1].inspected


print(day11a())
print(day11b())
