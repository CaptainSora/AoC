from collections import deque


def day06a():
	with open("2021/day06_input.txt", "r") as f:
		lantern = [int(num) for num in f.read().strip().split(",")]
	ages = deque([lantern.count(i) for i in range(9)])
	for _ in range(80):
		ages.rotate(-1)
		ages[6] += ages[-1]
	return(sum(ages))

def day06b():
	with open("2021/day06_input.txt", "r") as f:
		lantern = [int(num) for num in f.read().strip().split(",")]
	ages = deque([lantern.count(i) for i in range(9)])
	for _ in range(256):
		ages.rotate(-1)
		ages[6] += ages[-1]
	return(sum(ages))


print(day06a())
print(day06b())
