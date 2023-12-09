def day01a():
	with open("2023/day01_input.txt", "r") as f:
		lines = f.read().strip().split("\n")
	calibration = 0
	for line in lines:
		nums = [int(d) for d in line if d.isdigit()]
		calibration += 10 * nums[0] + nums[-1]
	return calibration


def day01b():
	with open("2023/day01_input.txt", "r") as f:
		lines = f.read().strip().split("\n")
	calibration = 0
	digits = [
		"one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
		"1", "2", "3", "4", "5", "6", "7", "8", "9"
	]
	for line in lines:
		left = [line.find(d) for d in digits]
		right = [line.rfind(d) for d in digits]
		l_idx = left.index(min([n for n in left if n > -1]))
		r_idx = right.index(max(right))
		calibration += ((l_idx % 9) + 1) * 10 + (r_idx % 9) + 1
		### First version:
		# front, end = 1, -1
		# while True:
		# 	pos = [line[:front].find(n) for n in digits]
		# 	if max(pos) > -1:
		# 		idx = pos.index(max(pos))
		# 		calibration += ((idx % 9) + 1) * 10
		# 		break
		# 	front += 1
		# while True:
		# 	pos = [line[end:].find(n) for n in digits]
		# 	if max(pos) > -1:
		# 		idx = pos.index(max(pos))
		# 		calibration += (idx % 9) + 1
		# 		break
		# 	end -= 1
	return calibration


print(day01a())
print(day01b())
