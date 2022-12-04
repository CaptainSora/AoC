def day11a():
	with open("2020/day11_input.txt", "r") as f:
		seats = f.read().strip().split('\n')

	rows = len(seats)
	cols = len(seats[0])

	def count_adj(row, col):
		count = 0
		for i in range(-1, 2):
			for j in range(-1, 2):
				if i == 0 and j == 0:
					continue
				if row + i >= 0 and row + i < rows \
						and col + j >= 0 and col + j < cols:
					if seats[row+i][col+j] == "#":
						count += 1
		return count
	
	while True:
		newseats = []
		for i in range(rows):
			newrow = ""
			for j in range(cols):
				if seats[i][j] == "L" and count_adj(i, j) == 0:
					newrow += "#"
				elif seats[i][j] == "#" and count_adj(i, j) >= 4:
					newrow += "L"
				else:
					newrow += seats[i][j]
			newseats.append(newrow)
		if seats == newseats:
			return sum([row.count("#") for row in seats])
		seats = newseats

def day11b():
	with open("2020/day11_input.txt", "r") as f:
		seats = f.read().strip().split('\n')

	rows = len(seats)
	cols = len(seats[0])

	def count_adj(row, col):
		count = 0
		for i in range(-1, 2):
			for j in range(-1, 2):
				if i == 0 and j == 0:
					continue
				r, c = i, j
				while row + r >= 0 and row + r < rows \
						and col + c >= 0 and col + c < cols:
					if seats[row+r][col+c] == ".":
						r += i
						c += j
						continue
					elif seats[row+r][col+c] == "#":
						count += 1
					break
		return count

	while True:
		newseats = []
		for i in range(rows):
			newrow = ""
			for j in range(cols):
				if seats[i][j] == "L" and count_adj(i, j) == 0:
					newrow += "#"
				elif seats[i][j] == "#" and count_adj(i, j) >= 5:
					newrow += "L"
				else:
					newrow += seats[i][j]
			newseats.append(newrow)
		if seats == newseats:
			return sum([row.count("#") for row in seats])
		seats = newseats


print(day11a())
print(day11b())
