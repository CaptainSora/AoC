from collections import Counter


def day07a():
	with open("2023/day07_input.txt", "r") as f:
		games = [line.strip().split() for line in f.read().strip().split("\n")]
	
	def score(hand):
		"""
		Gives a score to each hand. Only comparable with other hands of the
		same type.
		"""
		score_dict = {
			"A": 12, "K": 11, "Q": 10, "J": 9, "T": 8, "9": 7, "8": 6,
			"7": 5, "6": 4, "5": 3, "4": 2, "3": 1, "2": 0
		}
		return sum([
			score_dict[hand[i]] * pow(13, 4 - i)
			for i in range(len(hand))
		])

	hand_types = {
		"hc": [], "1p": [], "2p": [], "3k": [], "fh": [], "4k": [], "5k": []
	}

	for hand, bet in games:
		grouped = Counter(hand).most_common()
		if len(grouped) == 1:
			hand_types["5k"].append((hand, int(bet)))
		elif len(grouped) == 2:
			if grouped[0][1] == 4:
				hand_types["4k"].append((hand, int(bet)))
			else:
				hand_types["fh"].append((hand, int(bet)))
		elif len(grouped) == 3:
			if grouped[0][1] == 3:
				hand_types["3k"].append((hand, int(bet)))
			else:
				hand_types["2p"].append((hand, int(bet)))
		elif len(grouped) == 4:
			hand_types["1p"].append((hand, int(bet)))
		else:
			hand_types["hc"].append((hand, int(bet)))
	
	winnings = 0
	rank = 1
	for _, hands in hand_types.items():
		hands.sort(key=lambda x: score(x[0]))
		for hand in hands:
			winnings += rank * hand[1]
			rank += 1
	return winnings
		

def day07b():
	with open("2023/day07_input.txt", "r") as f:
		games = [line.strip().split() for line in f.read().strip().split("\n")]
	
	def score(hand):
		"""
		Gives a score to each hand. Only comparable with other hands of the
		same type.
		"""
		score_dict = {
			"A": 12, "K": 11, "Q": 10, "T": 9, "9": 8, "8": 7, "7": 6,
			"6": 5, "5": 4, "4": 3, "3": 2, "2": 1, "J": 0
		}
		return sum([
			score_dict[hand[i]] * pow(13, 4 - i)
			for i in range(len(hand))
		])

	hand_types = {
		"hc": [], "1p": [], "2p": [], "3k": [], "fh": [], "4k": [], "5k": []
	}

	for hand, bet in games:
		hand_dict = Counter(hand)
		if "J" in hand_dict:
			for card_type in hand_dict:
				if card_type != "J":
					hand_dict[card_type] += hand_dict["J"]
			if len(hand_dict) > 1:
				hand_dict.pop("J")
		grouped = hand_dict.most_common()

		if len(grouped) == 1:
			hand_types["5k"].append((hand, int(bet)))
		elif len(grouped) == 2:
			if grouped[0][1] == 4:
				hand_types["4k"].append((hand, int(bet)))
			else:
				hand_types["fh"].append((hand, int(bet)))
		elif len(grouped) == 3:
			if grouped[0][1] == 3:
				hand_types["3k"].append((hand, int(bet)))
			else:
				hand_types["2p"].append((hand, int(bet)))
		elif len(grouped) == 4:
			hand_types["1p"].append((hand, int(bet)))
		else:
			hand_types["hc"].append((hand, int(bet)))
	
	winnings = 0
	rank = 1
	for _, hands in hand_types.items():
		hands.sort(key=lambda x: score(x[0]))
		for hand in hands:
			winnings += rank * hand[1]
			rank += 1
	return winnings


print(day07a())
print(day07b())
