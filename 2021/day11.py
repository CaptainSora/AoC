from collections import deque
from itertools import count


def day11a():
	with open("2021/day11_input.txt", "r") as f:
		octo = [
			[int(num) for num in row]
			for row in f.read().strip().split("\n")
		]
	nrow, ncol = len(octo), len(octo[0])
	flashes = 0
	for _ in range(100):
		flashq = deque()
		octo = [[num + 1 for num in row] for row in octo]
		flashq.extend([
			(r, c) for r in range(nrow) for c in range(ncol)
			if octo[r][c] == 10
		])
		while flashq:
			fr, fc = flashq.popleft()
			flashes += 1
			for r in [fr-1, fr, fr+1]:
				if r < 0 or r >= nrow:
					continue
				for c in [fc-1, fc, fc+1]:
					if c < 0 or c >= ncol:
						continue
					octo[r][c] += 1
					if octo[r][c] == 10:
						flashq.append((r, c))
		octo = [[num if num < 10 else 0 for num in row] for row in octo]
	return flashes


def day11b():
	with open("2021/day11_input.txt", "r") as f:
		octo = [
			[int(num) for num in row]
			for row in f.read().strip().split("\n")
		]
	nrow, ncol = len(octo), len(octo[0])
	for step in count(1):
		stepflashes = 0
		flashq = deque()
		octo = [[num + 1 for num in row] for row in octo]
		flashq.extend([
			(r, c) for r in range(nrow) for c in range(ncol)
			if octo[r][c] == 10
		])
		while flashq:
			fr, fc = flashq.popleft()
			stepflashes += 1
			for r in [fr-1, fr, fr+1]:
				if r < 0 or r >= nrow:
					continue
				for c in [fc-1, fc, fc+1]:
					if c < 0 or c >= ncol:
						continue
					octo[r][c] += 1
					if octo[r][c] == 10:
						flashq.append((r, c))
		octo = [[num if num < 10 else 0 for num in row] for row in octo]
		if stepflashes == nrow * ncol:
			return step


print(day11a())
print(day11b())
