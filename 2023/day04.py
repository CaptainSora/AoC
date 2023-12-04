def day04a():
	with open("2023/day04_input.txt", "r") as f:
		cards = f.read().strip().split("\n")
	total_pts = 0
	for card in cards:
		_, winning, hand = card.replace(":", " |").split(" | ")
		winning = set([int(num) for num in winning.split() if num])
		hand = set([int(num) for num in hand.split() if num])
		match = winning & hand
		if match:
			total_pts += pow(2, len(match) - 1)
	return total_pts


def day04b():
	with open("2023/day04_input.txt", "r") as f:
		cards = f.read().strip().split("\n")
	copies = [1 for _ in cards]
	for card in cards:
		title, winning, hand = card.replace(":", " |").split(" | ")
		cardnum = int(title.split()[-1]) - 1
		winning = set([int(num) for num in winning.split() if num])
		hand = set([int(num) for num in hand.split() if num])
		match = winning & hand
		for idx in range(cardnum + 1, cardnum + 1 + len(match)):
			copies[idx] += copies[cardnum]
	return sum(copies)


print(day04a())
print(day04b())
