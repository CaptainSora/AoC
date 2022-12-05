from itertools import compress


class Bingo:
	def __init__(self, board):
		self.numbers = [int(num) for num in board.split() if num != ""]
		self.stamps = [False] * 25
	
	def check(self, num):
		try:
			idx = self.numbers.index(num)
		except ValueError:
			pass
		else:
			self.stamps[idx] = True
	
	def win(self):
		return any([
			all(self.stamps[:5]),
			all(self.stamps[5:10]),
			all(self.stamps[10:15]),
			all(self.stamps[15:20]),
			all(self.stamps[20:]),
			all(self.stamps[::5]),
			all(self.stamps[1::5]),
			all(self.stamps[2::5]),
			all(self.stamps[3::5]),
			all(self.stamps[4::5])
		])
	
	def unmarked(self):
		return sum(self.numbers) - sum(compress(self.numbers, self.stamps))


def day04a():
	with open("2021/day04_input.txt", "r") as f:
		numbers, *boards = f.read().split("\n\n")
	numbers = [int(num) for num in numbers.split(",")]
	bingos = [Bingo(b) for b in boards]
	for num in numbers:
		for board in bingos:
			board.check(num)
			if board.win():
				return num * board.unmarked()

def day04b():
	with open("2021/day04_input.txt", "r") as f:
		numbers, *boards = f.read().split("\n\n")
	numbers = [int(num) for num in numbers.split(",")]
	bingos = [Bingo(b) for b in boards]
	completed = [False for _ in boards]
	for num in numbers:
		for i in range(len(bingos)):
			bingos[i].check(num)
			if bingos[i].win():
				completed[i] = True
			if all(completed):
				return num * bingos[i].unmarked()


print(day04a())
print(day04b())
