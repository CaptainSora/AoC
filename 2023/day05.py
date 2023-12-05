# https://adventofcode.com/2023/leaderboard/day/5


def day05a():
	with open("2023/day05_input.txt", "r") as f:
		seeds, *maps = f.read().strip().split("\n\n")
	seeds = [int(s) for s in seeds.split()[1:] if s]
	for map in maps:
		lines = [
			[int(num) for num in line.strip().split()]
			for line in map.strip().split("\n")[1:]\
		]
		lines.sort(key=lambda x: x[1])
		for idx, s in enumerate(seeds):
			for line in lines:
				if line[1] <= s < line[1] + line[2]:
					seeds[idx] += line[0] - line[1]
					break
	return min(seeds)


def day05b():
	with open("2023/day05_input.txt", "r") as f:
		seeds, *maps = f.read().strip().split("\n\n")
	seeds = [int(s) for s in seeds.split()[1:] if s]
	seeds = [
		[seeds[i], seeds[i] + seeds[i+1] - 1]
		for i in range(0, len(seeds), 2)
	]
	for map in maps:
		lines = [
			[int(num) for num in line.strip().split()]
			for line in map.strip().split("\n")[1:]\
		]
		lines.sort(key=lambda x: x[1])
		new_seeds = []
		while seeds:
			start, end = seeds.pop(0)
			for line in lines:
				if line[1] <= start < line[1] + line[2]:
					range_end = line[1] + line[2] - 1
					offset = line[0] - line[1]
					new_seeds.append(
						[start + offset, min(end, range_end) + offset]
					)
					if range_end < end:
						start = range_end + 1
					else:
						break
			else:
				new_seeds.append([start, end])
		seeds = new_seeds
	return min([seed[0] for seed in seeds])


print(day05a())
print(day05b())
