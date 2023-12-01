from collections import deque, namedtuple


class State:
	def __init__(self, costs, time=0, mats=[0, 0, 0, 0], robots=[1, 0, 0, 0]):
		self.costs = costs
		self.time = time
		self.mats = mats # Ore, clay, obsidian, geode
		self.robots = robots
	
	def copy(self):
		return State(self.costs[:], self.time, self.mats[:], self.robots[:])
	
	def id(self):
		return tuple([self.time] + self.robots)
	
	def collect(self):
		for i in range(4):
			self.mats[i] += self.robots[i]
		self.time += 1
	
	def ore(self):
		if self.mats[0] >= self.costs[0]:
			newState = self.copy()
			newState.mats[0] -= self.costs[0]
			newState.collect()
			newState.robots[0] += 1
			return newState
		return None
	
	def clay(self):
		if self.mats[0] >= self.costs[1]:
			newState = self.copy()
			newState.mats[0] -= self.costs[1]
			newState.collect()
			newState.robots[1] += 1
			return newState
		return None
	
	def obsidian(self):
		if self.mats[0] >= self.costs[2] and self.mats[1] >= self.costs[3]:
			newState = self.copy()
			newState.mats[0] -= self.costs[2]
			newState.mats[1] -= self.costs[3]
			newState.collect()
			newState.robots[2] += 1
			return newState
		return None
	
	def geode(self):
		if self.mats[0] >= self.costs[4] and self.mats[2] >= self.costs[5]:
			newState = self.copy()
			newState.mats[0] -= self.costs[4]
			newState.mats[2] -= self.costs[5]
			newState.collect()
			newState.robots[3] += 1
			return newState
		return None
	
	def options(self):
		# Always make a geode robot when possible
		geo = self.geode()
		if geo is not None:
			return [geo]
		# Always make an obsidian robot when possible, if there are none
		obs = self.obsidian()
		if self.robots[2] == 0 and obs is not None:
			return [obs]
		# Always make a clay robot when possible, if there are none
		cla = self.clay()
		if self.robots[1] == 0 and cla is not None:
			return [cla]
		# Return every other feasible option
		options = [
			opt for opt in [obs, cla, self.ore()]
			if opt is not None
		]
		self.collect()
		options.append(self)
		return options


def day19a():
	with open("2022/day19_input.txt", "r") as f:
		blueprints = [
			[int(num) for num in line.split() if num.isdigit()]
			for line in f.read().strip().split("\n")
		]
	quality = 0
	bp_num = 0
	for line in blueprints:
		best = [0 for _ in range(24)]
		bp_num += 1
		q = deque([State(line)])
		max_geo = 0
		while q:
			s = q.popleft()
			# Finish
			if s.time == 24:
				max_geo = max(max_geo, s.mats[3])
				continue
			# Prune
			if s.robots[3] >= best[s.time]:
				best[s.time] = s.robots[3]
			else:
				continue
			print(s.time, s.mats, s.robots)
			q.extend(s.options())
		print(max_geo)
		break



def day19b():
	with open("2022/day19_input.txt", "r") as f:
		pass


print(day19a())
print(day19b())
