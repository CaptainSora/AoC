def day09a():
	with open("2023/day09_input.txt", "r") as f:
		histories = f.read().strip().split("\n")
	
	def diffs(hist):
		d = [hist[i] - hist[i-1] for i in range(1, len(hist))]
		if not any(d):
			return hist[-1]
		d.append(diffs(d))
		return hist[-1] + d[-1]
	
	ext_val_sum = 0
	for line in histories:
		ext_val_sum += diffs([int(num) for num in line.strip().split()])
	return ext_val_sum


def day09b():
	with open("2023/day09_input.txt", "r") as f:
		histories = f.read().strip().split("\n")
	
	def diffs(hist):
		d = [hist[i] - hist[i-1] for i in range(1, len(hist))]
		if not any(d):
			return hist[-1]
		d.append(diffs(d))
		return hist[-1] + d[-1]
	
	ext_val_sum = 0
	for line in histories:
		ext_val_sum += diffs([int(num) for num in line.strip().split()][::-1])
	return ext_val_sum


print(day09a())
print(day09b())
