def day02a():
	with open("2023/day02_input.txt", "r") as f:
		games = f.read().strip().split("\n")
	valid_games = 0
	bag = {"red": 12, "green": 13, "blue": 14}
	for game in games:
		header, draws = game.strip().split(": ")
		game_id = int(header.split()[1])
		draws = draws.split("; ")
		# Try for-else block for fun :)
		for draw in draws:
			colors = draw.split(", ")
			for color in colors:
				num, col = color.split()
				if int(num) > bag[col]:
					break
			else: # nobreak
				continue
			break
		else: # nobreak
			valid_games += game_id
	return valid_games


def day02b():
	with open("2023/day02_input.txt", "r") as f:
		games = f.read().strip().split("\n")
	game_powers = 0
	for game in games:
		header, draws = game.strip().split(": ")
		colors = draws.replace(";", ",").split(", ")
		bag = {"red": 0, "green": 0, "blue": 0}
		for color in colors:
			num, col = color.split()
			bag[col] = max(bag[col], int(num))
		game_powers += bag["red"] * bag["green"] * bag["blue"]
	return game_powers


print(day02a())
print(day02b())
