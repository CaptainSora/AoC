def day25a():
	with open("2020/day25_input.txt", "r") as f:
		cpub, dpub = [int(num) for num in f.read().strip().split('\n')]
	
	def get_loop_size(pub):
		value = 1
		loops = 0
		while value != pub:
			value = (value * 7) % 20201227
			loops += 1
		return loops
	
	def transform(pub, loop):
		value = 1
		for _ in range(loop):
			value = (value * pub) % 20201227
		return value
	
	cloop = get_loop_size(cpub)
	return transform(dpub, cloop)

def day25b():
	return True


print(day25a())
print(day25b())
