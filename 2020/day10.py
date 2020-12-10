def day10a():
	with open("2020/day10_input.txt", "r") as f:
		adapters = [int(num) for num in f.read().strip().split('\n')]
	
	adapters.sort()
	diff = [0, 1, 0, 1]
	for a in range(1, len(adapters)):
		diff[adapters[a] - adapters[a-1]] += 1
	return diff[1] * diff[3]


def day10b():
	with open("2020/day10_input.txt", "r") as f:
		adapters = [int(num) for num in f.read().strip().split('\n')]
	
	adapters.append(0)
	adapters.append(max(adapters) + 3)
	adapters.sort()
	adapters = adapters[::-1]
	combos = [1]
	for a in range(1, len(adapters)):
		newcombos = 0
		for i in range(1, 4):
			if adapters[a] + i in adapters:
				newcombos += combos[adapters.index(adapters[a] + i)]
		combos.append(newcombos)
	return combos[-1]


print(day10b())
