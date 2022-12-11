from copy import copy
from queue import PriorityQueue


class BossFight:
	def __init__(self, bhp, batk, hard=False):
		self.bosshp = bhp # 51
		self.batk = batk # 9
		self.hp = 50
		self.mana = 500
		self.mana_spent = 0
		self.costs = (53, 73, 113, 173, 229)
		self.shield = 0
		self.poison = 0
		self.recharge = 0
		self.hard = hard
	
	def __lt__(self, other):
		return self.mana_spent < other.mana_spent
	
	def apply_effects(self):
		# Apply effects and decrement timers
		if self.shield:
			self.shield -= 1
		if self.poison:
			self.bosshp -= 3
			self.poison -= 1
		if self.recharge:
			self.mana += 101
			self.recharge -= 1
	
	def choose_action(self):
		"""
		Returns a list of BossFight instances with every possible action.
		"""
		# Generate new possible actions
		next = []
		for i in range(5):
			if self.mana < self.costs[i]:
				break
			new = copy(self)
			if i == 0:
				new.bosshp -= 4
			elif i == 1:
				new.bosshp -= 2
				new.hp += 2
			elif i == 2:
				if new.shield:
					continue
				else:
					new.shield = 6
			elif i == 3:
				if new.poison:
					continue
				else:
					new.poison = 6
			elif i == 4:
				if new.recharge:
					continue
				else:
					new.recharge = 5
			new.mana -= new.costs[i]
			new.mana_spent += new.costs[i]
			new.boss_turn()
			if new.hp > 0:
				next.append(new)
		return next
	
	def boss_turn(self):
		self.apply_effects()
		if self.bosshp > 0:
			self.hp -= max(1, self.batk - 7 * (self.shield > 0))
	
	def player_turn(self):
		"""
		Returns win, listof(BossFight)
		"""
		self.apply_effects()
		if self.hard:
			self.hp -= 1
			if self.hp <= 0:
				return False, []
		if self.bosshp <= 0:
			return True, []
		return False, self.choose_action()


def day22a():
	with open("2015/day22_input.txt", "r") as f:
		bhp, batk = [int(num) for num in f.read().split()[2::2]]
	q = PriorityQueue()
	q.put_nowait(BossFight(bhp, batk))
	while not q.empty():
		state = q.get_nowait()
		win, next = state.player_turn()
		if win:
			return state.mana_spent
		for n in next:
			q.put_nowait(n)

def day22b():
	with open("2015/day22_input.txt", "r") as f:
		bhp, batk = [int(num) for num in f.read().split()[2::2]]
	q = PriorityQueue()
	q.put_nowait(BossFight(bhp, batk, hard=True))
	while not q.empty():
		state = q.get_nowait()
		win, next = state.player_turn()
		if win:
			return state.mana_spent
		for n in next:
			q.put_nowait(n)


print(day22a())
print(day22b())
