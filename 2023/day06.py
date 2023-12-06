from math import prod


def day06a():
	with open("2023/day06_input.txt", "r") as f:
		time, distance = [
			[int(num) for num in line.split()[1:] if num]
			for line in f.read().strip().split("\n")
		]
	win_options = [0 for _ in distance]
	for hold_dur in range(1, time[-1]):
		for idx, t in enumerate(time):
			dist = hold_dur * (t - hold_dur)
			if dist > distance[idx]:
				win_options[idx] += 1
	return prod(win_options)


def day06b():
	with open("2023/day06_input.txt", "r") as f:
		time, distance = [
			int(line.split(":")[-1])
			for line in f.read().strip().replace(" ", "").split("\n")
		]
	print(time, distance)
	winners = []
	for hold_dur in range(1, time):
		dist = hold_dur * (time - hold_dur)
		if dist > distance:
			winners.append(hold_dur)
			break
	for hold_dur in range(time, 1, -1):
		dist = hold_dur * (time - hold_dur)
		if dist > distance:
			winners.append(hold_dur)
			break
	return winners[1] - winners[0] + 1


print(day06a())
print(day06b())
