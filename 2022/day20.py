def day20a():
	with open("2022/day20_input.txt", "r") as f:
		nums = [int(num) for num in f.read().strip().split("\n")]
	file = nums[:]
	for n in nums:
		s = file.index(n)
		e = (s + n) % (len(nums) - 1)
		if e != s:
			file.pop(s)
			file.insert(e, n)
	zero = file.index(0)
	return sum([file[(zero + k) % len(nums)] for k in [1000, 2000, 3000]])

def day20b():
	with open("2022/day20_input.txt", "r") as f:
		pass


print(day20a())
print(day20b())
